from datetime import datetime, timedelta
from app.domain.resource import Resource
from app.domain.snapshot import Snapshot
from app.domain.retention_plan import RetentionPlan
from app.service.retention_plan_service import should_retain_snapshot
from uuid import uuid4

SNAPSHOT = Snapshot(Resource("RDS"))

if __name__ == "__main__":
    x = uuid4() # adicionar uuid após as outras coisas
    print(x)
    # retention_plan = RetentionPlan(SNAPSHOT, "standard")
    # print(should_retain_snapshot(retention_plan))

    # retention_plan = RetentionPlan(SNAPSHOT, "gold")
    # print(should_retain_snapshot(retention_plan))

    # retention_plan = RetentionPlan(SNAPSHOT, "platinum")
    # print(should_retain_snapshot(retention_plan))
