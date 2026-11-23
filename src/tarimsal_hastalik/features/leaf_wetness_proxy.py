
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[3]

INPUT_PATH = (
    PROJECT_ROOT / "data" / "processed" / "weather"
    / "nigde_2026-04_features.csv"
)

OUTPUT_PATH = (
    PROJECT_ROOT / "data" / "processed" / "weather"
    / "nigde_2026-04_leaf_wetness_proxy.csv"
)

# Geçici başlangıç parametresi.
# Uzman görüşü ve bilimsel kaynaklarla daha sonra güncellenecek.
HUMIDITY_THRESHOLD = 90.0



def create_leaf_wetness_proxy():
    df = pd.read_csv(INPUT_PATH)

    required_columns = [
        "time",
        "relative_humidity_2m",
        "precipitation"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Eksik sütunlar: {missing_columns}")

    df["time"] = pd.to_datetime(df["time"])
    df = df.sort_values("time").reset_index(drop=True)

    df["rain_wetness_indicator"] = (
        df["precipitation"] > 0
    )

    # Yüksek nem, ancak yağışla başlayan dönem devam ediyorsa
    # potansiyel ıslaklık göstergesine katkı sağlar.
    potential_wetness = []
    wetness_evidence = []
    rain_period_active = False

    for _, row in df.iterrows():
        is_raining = row["rain_wetness_indicator"]
        humidity = row["relative_humidity_2m"]

        if is_raining:
            rain_period_active = True
            potential_wetness.append(True)
            wetness_evidence.append("rain")

        elif rain_period_active and humidity >= HUMIDITY_THRESHOLD:
            potential_wetness.append(True)
            wetness_evidence.append("rain_followed_by_high_humidity")

        else:
            rain_period_active = False
            potential_wetness.append(False)
            wetness_evidence.append("none")

    df["potential_wetness_hour"] = potential_wetness
    df["wetness_evidence"] = wetness_evidence

    # Ardışık potansiyel ıslaklık saatlerini say.
    group_ids = (~df["potential_wetness_hour"]).cumsum()
    df["potential_wetness_duration_hours"] = 0

    wet_mask = df["potential_wetness_hour"]

    df.loc[wet_mask, "potential_wetness_duration_hours"] = (
        df.loc[wet_mask]
        .groupby(group_ids[wet_mask])
        .cumcount() + 1
    )

    df.to_csv(OUTPUT_PATH, index=False)

    print("Yağışla başlayan yaprak ıslaklığı göstergesi oluşturuldu.")
    print(f"Toplam kayıt: {len(df)}")
    print(
        "Potansiyel ıslaklık saati:",
        int(df["potential_wetness_hour"].sum())
    )
    print(
        "En uzun ardışık dönem:",
        int(df["potential_wetness_duration_hours"].max()),
        "saat"
    )

    print("\nGösterge kaynakları:")
    print(df["wetness_evidence"].value_counts())

    print(f"\nDosya kaydedildi: {OUTPUT_PATH}")


if __name__ == "__main__":
    create_leaf_wetness_proxy()
