import sys
from dotenv import load_dotenv
load_dotenv()
import os
sys.path.append(os.getenv("PATH_ROOT"))

import pytest
import json
from pynearmap.Coverage.Polygon import Polygon


@pytest.fixture
def polygon_instance():
    return Polygon()

def test_polygon_request(polygon_instance: Polygon):
    polygon_coord = [138.59707796614592, -34.91729448760797,
               138.61703360121672, -34.91729448760797,
               138.61703360121672, -34.927709974005474,
               138.59707796614592, -34.927709974005474,
               138.59707796614592, -34.91729448760797]
    polygon_instance.set_params(polygon=polygon_coord,
                       since="2015-07-01",
                       until="2019-03-20",
                       limit=1,
                       offset=1,
                       fields=['captureDate', 'firstPhotoTime', 'lastPhotoTime'],
                       sort="id"
                       )
    response = polygon_instance.call()

    assert response.status_code == 200
    assert response.ok == True

    assert response.json().get("limit") == 1
    assert response.json().get("offset") == 1
