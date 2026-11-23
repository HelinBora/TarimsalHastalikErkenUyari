
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[3]

INPUT_PATH = (
    PROJECT_ROOT / "data" / "processed" / "weather"
    / "nigde_2026-04_leaf_wetness_proxy.csv"
)

OUTPUT_PATH = (
    PROJECT_ROOT / "data" / "processed" / "weather"
    / "nigde_2026-04_wetness_episodes.csv"
)


def analyze_wetness_episodes():
    df = pd.read_csv(INPUT_PATH)
    df["time"] = pd.to_datetime(df["time"])

    # Her kesintisiz potansiyel ıslaklık dönemine bir grup numarası ver.
    group_ids = (~df["potential_wetness_hour"]).cumsum()

    wet_df = df[df["potential_wetness_hour"]].copy()
    wet_df["episode_id"] = group_ids[df["potential_wetness_hour"]]

    episodes = (
        wet_df.groupby("episode_id")
        .agg(
            start_time=("time", "min"),
            end_time=("time", "max"),
            duration_hours=("time", "count"),
            average_temperature=("temperature_2m", "mean"),
            average_humidity=("relative_humidity_2m", "mean"),
            total_precipitation=("precipitation", "sum"),
        )
        .reset_index(drop=True)
    )

    episodes.to_csv(OUTPUT_PATH, index=False)

    print("Islaklık dönemleri analiz edildi.")
    print(f"Toplam dönem sayısı: {len(episodes)}")

    print("\nEn uzun 10 dönem:")
    print(
        episodes.sort_values(
            "duration_hours", ascending=False
        ).head(10).to_string(index=False)
    )

    print(f"\nAnaliz dosyası: {OUTPUT_PATH}")


if __name__ == "__main__":
    analyze_wetness_episodes()
