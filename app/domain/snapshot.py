from datetime import datetime
from app.domain.resource import Resource

class Snapshot:
    """The state of a resource at a particular point in time.
    
    Parameter:
        resource (Resource): A Resource object.
    """
    def __init__(self, resource:Resource) -> None:
        if type(resource) is not Resource:
            raise TypeError("The resource name must be a Resource object.")
        self.__resource = resource
        self.__creation_date = datetime.now()
    
    def get_resource(self) -> Resource:
        """
        Gets the snapshot resource.

        Returns:
            A Resource object
        """
        return self.__resource
    
    def get_creation_date(self) -> datetime:
        """
        Gets the snapshot creation date.

        Returns:
            A datetime representing the snapshot creation date.
        """
        return self.__creation_date
