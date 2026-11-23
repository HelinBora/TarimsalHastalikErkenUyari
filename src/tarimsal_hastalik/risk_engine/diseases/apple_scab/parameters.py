
"""
Elma karalekesi enfeksiyon modeli parametreleri.

İlk uygulama adayı: Revised Mills Table.
Model, Türkiye koşullarında henüz doğrulanmamıştır.
"""

MODEL_METADATA = {
    "disease": "apple_scab",
    "scientific_name": "Venturia inaequalis",
    "model_name": "Revised Mills",
    "model_status": "research_candidate",
    "validation_status": "not_validated_for_turkey",
    "infection_type": "primary_ascospore",
}

MODEL_SOURCES = [
    {
        "authors": "MacHardy & Gadoury",
        "year": 1989,
        "description": "Mills kriterlerinin gözden geçirilmesi",
        "doi": "10.1094/Phyto-79-304",
    },
    {
        "authors": "Revised Mills Table",
        "year": None,
        "description": (
            "Sıcaklığa göre minimum yaprak ıslaklığı "
            "süreleri ve 8 saatlik birleştirme kuralı"
        ),
        "url": (
            "https://onfruit.ca/wp-content/uploads/"
            "2017/04/revised-mills-table.pdf"
        ),
    },
    {
        "authors": "Stensvand et al.",
        "year": 1997,
        "description": "Düşük sıcaklıklarda spor salımı ve enfeksiyon",
        "doi": "10.1094/PHYTO.1997.87.10.1046",
    },
    {
        "authors": "Rossi, Giosuè & Bugiani",
        "year": 2007,
        "description": "A-scab birincil enfeksiyon simülasyon modeli",
        "doi": "10.1111/j.1365-2338.2007.01125.x",
    },
]

# Sıcaklık (°C): minimum yaprak ıslaklığı süresi (saat).
# Kaynak tablodaki değerlerdir.
PRIMARY_INFECTION_WETNESS_HOURS = {
    1: 40.5,
    2: 34.7,
    3: 29.6,
    4: 27.8,
    5: 21.2,
    6: 18.0,
    7: 15.4,
    8: 13.4,
    9: 12.2,
    10: 11.0,
    11: 9.0,
    12: 8.3,
    13: 8.0,
    14: 7.0,
    15: 7.0,
    16: 6.1,
    17: 6.0,
    18: 6.0,
    19: 6.0,
    20: 6.0,
    21: 6.0,
    22: 6.0,
    23: 6.0,
    24: 6.1,
    25: 8.0,
    26: 11.3,
}

MODEL_PARAMETERS = {
    "max_dry_gap_hours": 8,
    "temperature_rounding": "nearest_integer",
    "primary_infection_wetness_hours": (
        PRIMARY_INFECTION_WETNESS_HOURS
    ),
}
