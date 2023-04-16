import pytest
from app.domain.resource import Resource

def test_valid_resource_name():
    resource = Resource("VPC")
    assert type(resource.get_resource_name()) == str

def test_invalid_resource_name():
    with pytest.raises(TypeError):
        resource = Resource(523.78)
