
from datetime import date

import pandas as pd
import requests


BASE_URL = "https://archive-api.open-meteo.com/v1/archive"


def get_hourly_weather(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """
    Open-Meteo üzerinden saatlik tarihsel meteorolojik
    verileri alır ve Pandas DataFrame olarak döndürür.
    """

    # Tarih kontrolleri
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)

    if start > end:
        raise ValueError("Başlangıç tarihi bitiş tarihinden sonra olamaz.")

    # Koordinat kontrolleri
    if not -90 <= latitude <= 90:
        raise ValueError("Enlem -90 ile 90 arasında olmalıdır.")

    if not -180 <= longitude <= 180:
        raise ValueError("Boylam -180 ile 180 arasında olmalıdır.")

    # API istek parametreleri
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
        ],
        "timezone": "Europe/Istanbul",
    }

    # API isteği
    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=30,
        )
        response.raise_for_status()

    except requests.RequestException as error:
        raise RuntimeError(
            f"Meteorolojik veri alınamadı: {error}"
        ) from error

    # JSON yanıtını işle
    data = response.json()

    if "hourly" not in data:
        raise ValueError("API yanıtında saatlik veri bulunamadı.")

    hourly_data = data["hourly"]

    # Pandas DataFrame oluştur
    df = pd.DataFrame({
        "time": hourly_data["time"],
        "temperature_2m": hourly_data["temperature_2m"],
        "relative_humidity_2m": hourly_data["relative_humidity_2m"],
        "precipitation": hourly_data["precipitation"],
    })

    df["time"] = pd.to_datetime(df["time"])

    return df
