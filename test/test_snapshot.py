import pytest
from datetime import datetime, timedelta
from app.domain.snapshot import Snapshot
from app.domain.resource import Resource

SNAPSHOT = Snapshot(Resource("VPC"))

def test_valid_resource_type():
    assert type(SNAPSHOT.get_resource()) == Resource

def test_invalid_resource_type():
    fake_source = "i wish i were a computing resource"
    with pytest.raises(TypeError):
        snapshot = Snapshot(fake_source)

def test_valid_creation_date():
    assert type(SNAPSHOT.get_creation_date()) == datetime

    yesterday = datetime.now() - timedelta(days=1)
    assert yesterday < SNAPSHOT.get_creation_date() 


