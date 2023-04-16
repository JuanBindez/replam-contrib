from datetime import datetime, timedelta
from app.domain.resource import Resource
from app.domain.snapshot import Snapshot
from app.domain.retention_plan import RetentionPlan
from app.service.retention_plan_service import should_retain_snapshot

SNAPSHOT = Snapshot(Resource("RDS"))

def test_should_retain_the_snapshot_when_no_date_is_passed():
    assert should_retain_snapshot(RetentionPlan(SNAPSHOT, "standard")) == True
    assert should_retain_snapshot(RetentionPlan(SNAPSHOT, "gold")) == True
    assert should_retain_snapshot(RetentionPlan(SNAPSHOT, "platinum")) == True
    

def test_should_retain_the_snapshot_when_date_is_passed():
    in_two_months = datetime.now() + timedelta(days=60)
    in_one_year = datetime.now() + timedelta(days=365)
    in_a_decade = datetime.now() + timedelta(days=3650)

    assert should_retain_snapshot(RetentionPlan(SNAPSHOT, "standard", in_two_months)) == True
    assert should_retain_snapshot(RetentionPlan(SNAPSHOT, "gold", in_one_year)) == True
    assert should_retain_snapshot(RetentionPlan(SNAPSHOT, "platinum", in_a_decade)) == True