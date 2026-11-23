
from pathlib import Path

import pandas as pd


# Proje ana dizini
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Girdi ve çıktı dosyaları
DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "weather"
    / "nigde_2026-04_clean.csv"
)

OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "weather"
    / "nigde_2026-04_features.csv"
)


def create_weather_features():
    # Temizlenmiş veriyi oku
    df = pd.read_csv(DATA_PATH)

    # Zaman sütununu datetime formatına dönüştür
    df["time"] = pd.to_datetime(df["time"])

    # Zamansal özellikler
    df["hour"] = df["time"].dt.hour
    df["day"] = df["time"].dt.day
    df["month"] = df["time"].dt.month

    # Yağış göstergesi
    # Bu özellik yağış olduğunu gösterir;
    # yaprak ıslaklığını kesin olarak kanıtlamaz.
    df["is_rain"] = df["precipitation"] > 0

    # Son 3 saatin hareketli ortalama sıcaklığı
    df["temperature_rolling_3h_mean"] = (
        df["temperature_2m"]
        .rolling(window=3, min_periods=1)
        .mean()
    )

    # Son 3 saatin hareketli ortalama nemi
    df["humidity_rolling_3h_mean"] = (
        df["relative_humidity_2m"]
        .rolling(window=3, min_periods=1)
        .mean()
    )

    # Mevcut saat dahil son 3 saatin toplam yağışı
    df["precipitation_rolling_3h_sum"] = (
        df["precipitation"]
        .rolling(window=3, min_periods=1)
        .sum()
    )

    # Özellikleri kaydet
    df.to_csv(OUTPUT_PATH, index=False)

    print("Feature Engineering tamamlandı.")
    print(f"Oluşturulan kayıt sayısı: {len(df)}")
    print("\nYeni özellikler:")
    print(df.columns.tolist())
    print(f"\nDosya kaydedildi: {OUTPUT_PATH}")


if __name__ == "__main__":
    create_weather_features()
