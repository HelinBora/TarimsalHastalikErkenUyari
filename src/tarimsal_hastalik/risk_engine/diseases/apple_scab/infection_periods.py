
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[5]

INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "weather"
    / "nigde_2026-04_leaf_wetness_proxy.csv"
)

OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "weather"
    / "nigde_2026-04_apple_scab_infection_periods.csv"
)

# Araştırma adayı kaynakta kullanılan geçici birleştirme kuralı.
MAX_DRY_GAP_HOURS = 8


def build_infection_periods():
    df = pd.read_csv(INPUT_PATH)

    required_columns = [
        "time",
        "temperature_2m",
        "potential_wetness_hour",
        "precipitation",
    ]

    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(f"Eksik sütunlar: {missing}")

    df["time"] = pd.to_datetime(df["time"])

    df["temperature_2m"] = pd.to_numeric(
        df["temperature_2m"], errors="coerce"
    )

    df["precipitation"] = pd.to_numeric(
        df["precipitation"], errors="coerce"
    )

    # CSV'den gelen True/False değerlerini güvenli biçimde dönüştür.
    if df["potential_wetness_hour"].dtype != bool:
        values = (
            df["potential_wetness_hour"]
            .astype(str)
            .str.strip()
            .str.lower()
        )

        mapping = {
            "true": True,
            "false": False,
            "1": True,
            "0": False,
        }

        df["potential_wetness_hour"] = values.map(mapping)

        if df["potential_wetness_hour"].isna().any():
            raise ValueError(
                "Islaklık göstergesinde geçersiz değer var."
            )

    if df["time"].isna().any():
        raise ValueError("Geçersiz zaman kaydı bulundu.")

    if df["temperature_2m"].isna().any():
        raise ValueError(
            "Sıcaklık verisinde eksik veya geçersiz değer var."
        )

    if df["precipitation"].isna().any():
        raise ValueError(
            "Yağış verisinde eksik veya geçersiz değer var."
        )

    df = df.sort_values("time").reset_index(drop=True)

    if df["time"].duplicated().any():
        raise ValueError("Tekrarlanan zaman kaydı bulundu.")

    # Saatlik zaman aralığını kontrol et.
    time_differences = df["time"].diff().dropna()

    if not (time_differences == pd.Timedelta(hours=1)).all():
        raise ValueError("Veriler kesintisiz saatlik aralıkta değil.")

    wet_indices = df.index[
        df["potential_wetness_hour"]
    ].tolist()

    periods = []
    current_indices = []

    for index in wet_indices:
        if current_indices:
            previous_index = current_indices[-1]

            time_difference = (
                df.loc[index, "time"]
                - df.loc[previous_index, "time"]
            )

            hours_difference = (
                time_difference.total_seconds() / 3600
            )

            dry_gap_hours = int(hours_difference) - 1

            if dry_gap_hours > MAX_DRY_GAP_HOURS:
                periods.append(current_indices)
                current_indices = []

        current_indices.append(index)

    if current_indices:
        periods.append(current_indices)

    results = []

    for period_number, indices in enumerate(periods, start=1):
        period_df = df.loc[indices]

        start_time = period_df["time"].iloc[0]
        end_time = period_df["time"].iloc[-1]

        # Sıcaklık istatistikleri yalnızca potansiyel ıslaklık
        # saatleri üzerinden hesaplanır.
        period_weather_df = period_df

        wet_hours = len(period_df)

        elapsed_hours = int(
            (end_time - start_time).total_seconds() / 3600
        ) + 1

        minimum_temperature = (
            period_weather_df["temperature_2m"].min()
        )

        maximum_temperature = (
            period_weather_df["temperature_2m"].max()
        )

        results.append({
            "period_id": period_number,
            "start_time": start_time,
            "end_time": end_time,
            "wet_hours": wet_hours,
            "elapsed_hours": elapsed_hours,
            "dry_gap_hours": elapsed_hours - wet_hours,
            "minimum_temperature": minimum_temperature,
            "maximum_temperature": maximum_temperature,
            "average_temperature_for_model": (
                minimum_temperature + maximum_temperature
            ) / 2,
            "total_precipitation": (
                period_weather_df["precipitation"].sum()
            ),
        })

    result_df = pd.DataFrame(results)

    result_df.to_csv(OUTPUT_PATH, index=False)

    print("Elma karalekesi enfeksiyon dönemleri oluşturuldu.")
    print("Toplam dönem:", len(result_df))
    print("Toplam ıslaklık saati:", result_df["wet_hours"].sum())
    print("Birleştirilen kuru saat:", result_df["dry_gap_hours"].sum())
    print(f"Dosya kaydedildi: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_infection_periods()
