
import pandas as pd

from src.tarimsal_hastalik.risk_engine.common.infection_model import InfectionModel
from src.tarimsal_hastalik.risk_engine.diseases.apple_scab.parameters import (
    MODEL_METADATA,
    MODEL_PARAMETERS,
)


class AppleScabModel(InfectionModel):
    """
    Elma karalekesi meteorolojik enfeksiyon eşik değerlendirme modeli.

    Revised Mills parametreleri araştırma adayıdır.
    Türkiye koşullarında henüz doğrulanmamıştır.

    Bu sınıf gerçek enfeksiyonu kanıtlamaz; yalnızca
    meteorolojik koşulların tanımlı eşikleri karşılayıp
    karşılamadığını değerlendirir.
    """

    REQUIRED_COLUMNS = [
        "period_id",
        "start_time",
        "end_time",
        "wet_hours",
        "average_temperature_for_model",
    ]

    def validate_input(self, weather_data: pd.DataFrame) -> None:
        if not isinstance(weather_data, pd.DataFrame):
            raise TypeError(
                "weather_data bir pandas DataFrame olmalıdır."
            )

        if weather_data.empty:
            raise ValueError("Enfeksiyon dönemi verisi boş olamaz.")

        missing_columns = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in weather_data.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Eksik sütunlar: {missing_columns}"
            )

        if weather_data["period_id"].duplicated().any():
            raise ValueError("Tekrarlanan period_id bulundu.")

        numeric_columns = [
            "wet_hours",
            "average_temperature_for_model",
        ]

        for column in numeric_columns:
            values = pd.to_numeric(
                weather_data[column],
                errors="coerce",
            )

            if values.isna().any():
                raise ValueError(
                    f"{column} sütununda geçersiz değer var."
                )

        if (weather_data["wet_hours"] <= 0).any():
            raise ValueError(
                "Islaklık süresi sıfırdan büyük olmalıdır."
            )

        if (
            pd.to_numeric(
                weather_data["wet_hours"],
                errors="coerce",
            ) % 1 != 0
        ).any():
            raise ValueError(
                "Islaklık saatleri tam sayı olmalıdır."
            )

        if pd.to_datetime(
            weather_data["start_time"],
            errors="coerce",
        ).isna().any():
            raise ValueError("Geçersiz başlangıç zamanı bulundu.")

        if pd.to_datetime(
            weather_data["end_time"],
            errors="coerce",
        ).isna().any():
            raise ValueError("Geçersiz bitiş zamanı bulundu.")

    def calculate_risk(
        self,
        weather_data: pd.DataFrame,
    ) -> pd.DataFrame:

        self.validate_input(weather_data)

        if not MODEL_PARAMETERS:
            raise RuntimeError(
                "Model parametreleri tanımlanmamış."
            )

        wetness_thresholds = MODEL_PARAMETERS.get(
            "primary_infection_wetness_hours"
        )

        if not wetness_thresholds:
            raise RuntimeError(
                "Birincil enfeksiyon ıslaklık eşikleri bulunamadı."
            )

        temperature_rounding = MODEL_PARAMETERS.get(
            "temperature_rounding"
        )

        if temperature_rounding != "nearest_integer":
            raise ValueError(
                "Desteklenmeyen sıcaklık yuvarlama yöntemi."
            )

        results = weather_data.copy()

        results["wet_hours"] = pd.to_numeric(
            results["wet_hours"]
        )

        results["average_temperature_for_model"] = pd.to_numeric(
            results["average_temperature_for_model"]
        )

        # Mevcut parametre dosyasındaki yuvarlama tercihi uygulanır.
        results["rounded_temperature"] = (
            results["average_temperature_for_model"]
            .round()
            .astype(int)
        )

        results["required_wet_hours"] = (
            results["rounded_temperature"]
            .map(wetness_thresholds)
        )

        results["threshold_met"] = (
            results["required_wet_hours"].notna()
            & (
                results["wet_hours"]
                >= results["required_wet_hours"]
            )
        )

        results["evaluation_status"] = "evaluated"

        results.loc[
            results["required_wet_hours"].isna(),
            "evaluation_status",
        ] = "temperature_out_of_model_range"

        results["risk_level"] = "wetness_threshold_not_met"

        results.loc[
            results["threshold_met"],
            "risk_level",
        ] = "wetness_threshold_met"

        results.loc[
            results["evaluation_status"]
            == "temperature_out_of_model_range",
            "risk_level",
        ] = "not_evaluated"

        results["model_name"] = MODEL_METADATA["model_name"]

        results["validation_status"] = (
            MODEL_METADATA["validation_status"]
        )

        results["explanation"] = results.apply(
            lambda row: (
                f"Ortalama sıcaklık: "
                f"{row['average_temperature_for_model']:.2f} °C. "
                f"Değerlendirme sıcaklığı: "
                f"{row['rounded_temperature']} °C. "
                f"Islaklık süresi: {row['wet_hours']} saat. "
                f"Gerekli süre: "
                f"{row['required_wet_hours']} saat. "
                + (
                    "Meteorolojik ıslaklık eşiği karşılandı."
                    if row["threshold_met"]
                    else "Meteorolojik ıslaklık eşiği karşılanmadı."
                )
            )
            if row["evaluation_status"] == "evaluated"
            else (
                "Sıcaklık, model tablosunun tanımlı aralığı dışında. "
                "Değerlendirme yapılamadı."
            ),
            axis=1,
        )

        return results
