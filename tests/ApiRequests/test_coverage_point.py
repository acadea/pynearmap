import sys
from dotenv import load_dotenv
load_dotenv()
import os
sys.path.append(os.getenv("PATH_ROOT"))
import pytest
from Src.Coverage.Point import Point

@pytest.fixture
def point_instance():
    return Point()

def test_point_request(point_instance: Point):
    point = [138.59707796614592,-34.91729448760797]
    point_instance.set_params(point=point,
                       since="2015-07-01",
                       until="2019-03-20",
                       limit=1,
                       offset=1,
                       fields=['captureDate', 'firstPhotoTime', 'lastPhotoTime'],
                       sort="id"
                       )
    response = point_instance.call()

    assert response.status_code == 200
    assert response.ok == True

    assert response.json().get("limit") == 1
    assert response.json().get("offset") == 1

