
import pandas as pd
from pathlib import Path


# Proje ana dizinini belirle
PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_PATH = (
    PROJECT_ROOT / "data" / "processed"
    / "weather" / "nigde_2026-04_clean.csv"
)


def validate_weather_data(file_path=DATA_PATH):
    """Temizlenmiş meteorolojik veriyi doğrular."""

    if not file_path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")

    df = pd.read_csv(file_path)

    print("\n--- METEOROLOJİK VERİ DOĞRULAMA ---")

    # 1. Kayıt sayısı
    print(f"\nToplam kayıt sayısı: {len(df)}")

    # 2. Eksik değer kontrolü
    print("\nEksik değerler:")
    print(df.isnull().sum())

    # 3. Tekrarlanan zaman kayıtları
    print(
        "\nTekrarlanan zaman kayıtları:",
        df["time"].duplicated().sum()
    )

    # 4. Saatlik aralık kontrolü
    timestamps = pd.to_datetime(df["time"])

    time_differences = timestamps.diff().dropna()

    invalid_intervals = (
        time_differences != pd.Timedelta(hours=1)
    ).sum()

    print(
        "Saatlik aralık dışında kalan kayıtlar:",
        invalid_intervals
    )

    # 5. Fiziksel sınır kontrolleri
    print(
        "Bağıl nem 0-100 dışında:",
        (~df["relative_humidity_2m"].between(0, 100)).sum()
    )

    print(
        "Negatif yağış kaydı:",
        (df["precipitation"] < 0).sum()
    )

    print(
        "Sıcaklık -50 ile 60°C dışında:",
        (~df["temperature_2m"].between(-50, 60)).sum()
    )

    # 6. Genel doğrulama sonucu
    is_valid = (
        df.notnull().all().all()
        and df["time"].is_unique
        and invalid_intervals == 0
        and df["relative_humidity_2m"].between(0, 100).all()
        and (df["precipitation"] >= 0).all()
        and df["temperature_2m"].between(-50, 60).all()
    )

    print("\nGenel doğrulama sonucu:")

    if is_valid:
        print("VERİ DOĞRULANDI.")
    else:
        print("VERİ DOĞRULAMADAN GEÇEMEDİ.")

    return is_valid


if __name__ == "__main__":
    validate_weather_data()
