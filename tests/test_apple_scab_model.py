
import pandas as pd
import pytest

from src.tarimsal_hastalik.risk_engine.diseases.apple_scab.model import (
    AppleScabModel,
)


@pytest.fixture
def model():
    return AppleScabModel()


@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "period_id": [1, 2],
        "start_time": [
            "2026-04-01 10:00:00",
            "2026-04-02 10:00:00",
        ],
        "end_time": [
            "2026-04-01 20:00:00",
            "2026-04-02 20:00:00",
        ],
        "wet_hours": [10, 5],
        "average_temperature_for_model": [12.0, 12.0],
    })


def test_threshold_met(model, sample_data):
    result = model.calculate_risk(sample_data)

    assert result.loc[0, "threshold_met"] == True
    assert result.loc[0, "risk_level"] == "wetness_threshold_met"


def test_threshold_not_met(model, sample_data):
    result = model.calculate_risk(sample_data)

    assert result.loc[1, "threshold_met"] == False
    assert result.loc[1, "risk_level"] == "wetness_threshold_not_met"


def test_temperature_out_of_model_range(model, sample_data):
    sample_data.loc[0, "average_temperature_for_model"] = 30.0

    result = model.calculate_risk(sample_data)

    assert result.loc[0, "evaluation_status"] == (
        "temperature_out_of_model_range"
    )
    assert result.loc[0, "risk_level"] == "not_evaluated"


def test_missing_column_raises_error(model, sample_data):
    sample_data = sample_data.drop(columns=["wet_hours"])

    with pytest.raises(ValueError, match="Eksik sütunlar"):
        model.calculate_risk(sample_data)


def test_empty_dataframe_raises_error(model):
    with pytest.raises(ValueError, match="boş olamaz"):
        model.calculate_risk(pd.DataFrame())
