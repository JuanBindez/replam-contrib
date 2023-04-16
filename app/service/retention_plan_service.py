from app.domain.retention_plan import RetentionPlan
from datetime import datetime, timedelta

def should_retain_snapshot(retention_plan:RetentionPlan) -> bool:
    """Checks if a snapshot should be retained based on its retention plan.

    Parameters:
        retention_plan (RetentionPlan): A RetentionPlan object.

    Returns:
        A boolean that indicates if the snapshot should be retained or not.
    """
    snapshot_date = retention_plan.get_creation_date()
    retention_plan_date = retention_plan.get_retention_date()
    retention_period = timedelta(days=42)
    
    if (snapshot_date + retention_period) > retention_plan_date:
        return False
    else:
        if retention_plan.get_retention_type() == "STANDARD":
            expiration_date = snapshot_date + retention_period
            return expiration_date >= datetime.now()

        else:
            last_day_of_month = (snapshot_date.replace(day=28) + timedelta(days=4)) \
                                    .replace(day=1) - timedelta(days=1)
            last_snapshot_of_month = last_day_of_month - timedelta(days=last_day_of_month.day)
            retention_period_monthly = timedelta(days=365)
            
            if retention_plan.get_retention_type() == "GOLD":
                if snapshot_date == last_snapshot_of_month:
                    retention_period += retention_period_monthly
                
                expiration_date = snapshot_date + retention_period
                return expiration_date >= datetime.now()
            
            else:
                last_snapshot_of_year = datetime(snapshot_date.year, 12, 31)
                retention_period_yearly = timedelta(days= 7 * 365)
                
                if snapshot_date == last_snapshot_of_month:
                    retention_period += retention_period_monthly
                if snapshot_date == last_snapshot_of_year:
                    retention_period += retention_period_yearly

                expiration_date = snapshot_date + retention_period
                return expiration_date >= datetime.now()