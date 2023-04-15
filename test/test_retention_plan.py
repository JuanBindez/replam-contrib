import pytest
from datetime import datetime, timedelta
from app.domain.resource import Resource
from app.domain.snapshot import Snapshot
from app.domain.retention_plan import RetentionPlan

RESOURCE = Resource("EC2")
SNAPSHOT = Snapshot(RESOURCE)

def test_invalid_retention_type():
    with pytest.raises(TypeError):
        retention_plan = RetentionPlan(SNAPSHOT,123)
    with pytest.raises(ValueError):
        retention_plan = RetentionPlan(SNAPSHOT, "abc")

def test_valid_retention_type():
    ret_plan_standard = RetentionPlan(SNAPSHOT,"standard")
    assert ret_plan_standard.get_retention_type() == "STANDARD"

    ret_plan_gold = RetentionPlan(SNAPSHOT,"gold")
    assert ret_plan_gold.get_retention_type() == "GOLD"

    ret_plan_platinum = RetentionPlan(SNAPSHOT,"platinum")
    assert ret_plan_platinum.get_retention_type() == "PLATINUM"

def test_retention_date():
    today = datetime.now()
    two_months_in_future = today + timedelta(days=60)
    ret_plan_standard = RetentionPlan(SNAPSHOT,"standard")

    assert today < ret_plan_standard.get_retention_date()
    assert two_months_in_future > ret_plan_standard.get_retention_date()
