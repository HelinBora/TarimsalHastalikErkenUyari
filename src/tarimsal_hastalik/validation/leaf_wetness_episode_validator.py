
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[3]

PROXY_PATH = (
    PROJECT_ROOT / "data" / "processed" / "weather"
    / "nigde_2026-04_leaf_wetness_proxy.csv"
)

EPISODE_PATH = (
    PROJECT_ROOT / "data" / "processed" / "weather"
    / "nigde_2026-04_wetness_episodes.csv"
)


def validate_wetness_episodes():
    df = pd.read_csv(PROXY_PATH)
    episodes = pd.read_csv(EPISODE_PATH)

    df["time"] = pd.to_datetime(df["time"])
    episodes["start_time"] = pd.to_datetime(episodes["start_time"])
    episodes["end_time"] = pd.to_datetime(episodes["end_time"])

    checks = {}

    # Kaynak verideki potansiyel ıslaklık saatleri
    source_wet_hours = int(
        df["potential_wetness_hour"].sum()
    )

    # Dönemlerdeki toplam saat
    episode_hours = int(
        episodes["duration_hours"].sum()
    )

    checks["Toplam dönem saati kaynakla eşleşiyor"] = (
        source_wet_hours == episode_hours
    )

    checks["Dönem sayısı doğru"] = (
        len(episodes) > 0
    )

    checks["Dönem süreleri pozitif"] = (
        (episodes["duration_hours"] > 0).all()
    )

    # Başlangıç ve bitiş zamanları arasındaki saat sayısı
    calculated_durations = (
        (episodes["end_time"] - episodes["start_time"])
        .dt.total_seconds() / 3600 + 1
    )

    checks["Dönem süreleri zaman aralığıyla eşleşiyor"] = (
        calculated_durations.eq(
            episodes["duration_hours"]
        ).all()
    )

    # Dönemler kronolojik ve birbiriyle çakışmıyor
    sorted_episodes = episodes.sort_values("start_time")

    no_overlap = (
        sorted_episodes["start_time"].iloc[1:].reset_index(drop=True)
        >
        sorted_episodes["end_time"].iloc[:-1].reset_index(drop=True)
    ).all()

    checks["Dönemler çakışmıyor"] = no_overlap

    print(f"Kaynak potansiyel ıslaklık saati: {source_wet_hours}")
    print(f"Dönemlerdeki toplam saat: {episode_hours}")
    print(f"Toplam dönem sayısı: {len(episodes)}")

    print("\nDoğrulama sonuçları:")

    for check_name, result in checks.items():
        print(f"{check_name}: {result}")

    if all(checks.values()):
        print("\nGENEL SONUÇ: DÖNEMLER DOĞRULANDI.")
    else:
        print("\nGENEL SONUÇ: DOĞRULAMA BAŞARISIZ.")


if __name__ == "__main__":
    validate_wetness_episodes()
