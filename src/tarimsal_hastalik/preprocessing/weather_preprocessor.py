
import pandas as pd
from pathlib import Path


# Proje ana dizinini belirle
PROJECT_ROOT = Path(__file__).resolve().parents[3]

RAW_DATA_PATH = (
    PROJECT_ROOT / "data" / "raw" / "weather"
    / "open_meteo" / "nigde_2026-04.csv"
)
PROCESSED_DATA_PATH = (
    PROJECT_ROOT / "data" / "processed"
    / "weather" / "nigde_2026-04_clean.csv"
)


REQUIRED_COLUMNS = [
    "time",
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation"
]


def load_weather_data(file_path=RAW_DATA_PATH):
    """Ham meteorolojik veriyi CSV dosyasından yükler."""

    if not file_path.exists():
        raise FileNotFoundError(f"Veri dosyası bulunamadı: {file_path}")

    df = pd.read_csv(file_path)

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Eksik sütunlar: {missing_columns}")

    return df


def preprocess_weather_data(df):
    """Meteorolojik veriyi temizler ve standartlaştırır."""

    df = df.copy()

    # Tarih bilgisini dönüştür
    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # Sayısal sütunları dönüştür
    numeric_columns = [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Geçersiz tarihleri kaldır
    df = df.dropna(subset=["time"])

    # Zaman sırasına göre sırala
    df = df.sort_values("time")

    # Tekrarlanan zaman kayıtlarını kaldır
    df = df.drop_duplicates(subset=["time"], keep="first")

    # Eksik meteorolojik değerleri kaldır
    df = df.dropna(subset=numeric_columns)

    # Fiziksel sınır kontrolleri
    df = df[
        (df["relative_humidity_2m"].between(0, 100)) &
        (df["precipitation"] >= 0) &
        (df["temperature_2m"].between(-50, 60))
    ]

    df = df.reset_index(drop=True)

    return df


def save_processed_data(df, output_path=PROCESSED_DATA_PATH):
    """Temizlenmiş veriyi CSV olarak kaydeder."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"Temizlenmiş veri kaydedildi: {output_path}")


def run_preprocessing():
    """Veri ön işleme sürecini çalıştırır."""

    raw_df = load_weather_data()

    print(f"İlk kayıt sayısı: {len(raw_df)}")

    processed_df = preprocess_weather_data(raw_df)

    print(f"Temizlenmiş kayıt sayısı: {len(processed_df)}")

    save_processed_data(processed_df)

    return processed_df


if __name__ == "__main__":
    run_preprocessing()
