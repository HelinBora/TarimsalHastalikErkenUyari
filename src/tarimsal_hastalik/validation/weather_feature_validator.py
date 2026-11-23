
from pathlib import Path

import pandas as pd


# Proje ana dizini
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Feature Engineering çıktısı
DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "weather"
    / "nigde_2026-04_features.csv"
)


def validate_weather_features():
    df = pd.read_csv(DATA_PATH)

    print(f"Toplam kayıt sayısı: {len(df)}")

    # Beklenen sütunlar
    required_columns = [
        "time",
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
        "hour",
        "day",
        "month",
        "is_rain",
        "temperature_rolling_3h_mean",
        "humidity_rolling_3h_mean",
        "precipitation_rolling_3h_sum",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    print("\nEksik sütunlar:", missing_columns)

    # Eksik değer kontrolü
    print("\nEksik değerler:")
    print(df[required_columns].isnull().sum())

    # Zaman sütununu dönüştür
    df["time"] = pd.to_datetime(df["time"])

    # Zamansal özellik kontrolleri
    hour_check = (df["hour"] == df["time"].dt.hour).all()
    day_check = (df["day"] == df["time"].dt.day).all()
    month_check = (df["month"] == df["time"].dt.month).all()

    print("\nZamansal özellik kontrolleri:")
    print("Saat bilgisi doğru:", hour_check)
    print("Gün bilgisi doğru:", day_check)
    print("Ay bilgisi doğru:", month_check)

    # Yağış göstergesi kontrolü
    rain_check = (
        df["is_rain"] == (df["precipitation"] > 0)
    ).all()

    print("\nYağış göstergesi doğru:", rain_check)

    # Hareketli ortalama kontrolü
    expected_temperature_mean = (
        df["temperature_2m"]
        .rolling(window=3, min_periods=1)
        .mean()
    )

    expected_humidity_mean = (
        df["relative_humidity_2m"]
        .rolling(window=3, min_periods=1)
        .mean()
    )

    expected_precipitation_sum = (
        df["precipitation"]
        .rolling(window=3, min_periods=1)
        .sum()
    )

    temperature_check = (
        df["temperature_rolling_3h_mean"]
        .round(6)
        == expected_temperature_mean.round(6)
    ).all()

    humidity_check = (
        df["humidity_rolling_3h_mean"]
        .round(6)
        == expected_humidity_mean.round(6)
    ).all()

    precipitation_check = (
        df["precipitation_rolling_3h_sum"]
        .round(6)
        == expected_precipitation_sum.round(6)
    ).all()

    print("\nHareketli özellik kontrolleri:")
    print("Sıcaklık ortalaması doğru:", temperature_check)
    print("Nem ortalaması doğru:", humidity_check)
    print("Yağış toplamı doğru:", precipitation_check)

    # Genel sonuç
    all_checks = [
        len(df) == 720,
        len(missing_columns) == 0,
        df[required_columns].isnull().sum().sum() == 0,
        hour_check,
        day_check,
        month_check,
        rain_check,
        temperature_check,
        humidity_check,
        precipitation_check,
    ]

    print("\nGenel doğrulama sonucu:")

    if all(all_checks):
        print("ÖZELLİKLER DOĞRULANDI.")
    else:
        print("DOĞRULAMA BAŞARISIZ. Kontrolleri inceleyin.")


if __name__ == "__main__":
    validate_weather_features()
