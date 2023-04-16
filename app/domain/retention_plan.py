from datetime import datetime, timedelta
from app.domain.snapshot import Snapshot

class RetentionPlan:
    """The snapshot's retention plan of a resource.
    
    Parameters:
        snapshot (Snapshot): A Snapshot object.
        retention_type (str): A string representing the type of the retention. Must be one of the 
        following: Standard, Gold or Platinum"
    """
    def __init__(self, snapshot:Snapshot, retention_type:str, creation_date:datetime = None):
        if type(snapshot) is not Snapshot:
            raise TypeError("The snapshot must be of a Snapshot type.")
        self.__resource_snapshot = snapshot

        if type(retention_type) is not str:
            raise TypeError("The retention type must be a string.")
        if retention_type.upper() not in ["STANDARD", "GOLD","PLATINUM"]:
            raise ValueError("The retention type must be one of the following: "
                             "Standard, Gold or Platinum")
        self.__retention_type = retention_type.upper()
        
        if creation_date and creation_date < datetime.now():
            raise ValueError("The retention date cannot not be in the past.")
        self.__creation_date = datetime.now()
        
        self.__retention_date = self.__creation_date + timedelta(days=42)
    
    def get_resource_snapshot(self) -> Snapshot:
        """
        Gets the resource snapshot of the retention plan.

        Returns:
        A Snapshot object.
          """
        return self.__resource_snapshot

    def get_retention_type(self) -> str:
        """
        Gets the retention type of the retention plan.

        Returns:
        A string representing the retention type.
        """          
        return self.__retention_type
    
    def get_creation_date(self) -> datetime:
        """
        Gets the creation date of the retention plan.

        Returns:
        A datetime representing the creation date.
        """          
        return self.__creation_date
    
    def get_retention_date(self) -> datetime:
        """
        Gets the retention date of the retention plan.

        Returns:
        A datetime representing the retention date.
        """          
        return self.__retention_date
