from abc import ABC, abstractmethod
import pandas as pd


class InfectionModel(ABC):
    """
    Tüm hastalık enfeksiyon modelleri için ortak arayüz.
    """

    @abstractmethod
    def calculate_risk(self, weather_data: pd.DataFrame) -> pd.DataFrame:
        """
        Meteorolojik verileri kullanarak enfeksiyon riskini hesaplar.

        Args:
            weather_data: İşlenmiş meteorolojik veriler.

        Returns:
            Enfeksiyon risk sonuçlarını içeren DataFrame.
        """
        pass