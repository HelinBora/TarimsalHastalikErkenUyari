from dataclasses import dataclass
from datetime import datetime


@dataclass
class RiskResult:
    """
    Hastalık risk modellerinin standart çıktı yapısı.
    """

    disease: str
    model_name: str
    start_time: datetime
    end_time: datetime
    risk_level: str
    risk_score: float | None
    explanation: str