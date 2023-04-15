class Resource:
    """A computing resource such as Server, Storage, Database, Network etc.
    
    Parameter:
        resource_name: A string representing the name of the resource.
    """
    def __init__(self, resource_name:str) -> None:
        self.__resource_name = resource_name
    
    def get_resource_name(self) -> str:
        """
        Gets the resource name.

        Returns:
            A string representing the name of the resource.
        """
        return self.__resource_name
