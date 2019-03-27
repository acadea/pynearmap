import sys
from dotenv import load_dotenv
load_dotenv()
import os
sys.path.append(os.getenv("PATH_ROOT"))
import pytest
from Src.Coverage.TileCoordinate import TileCoordinate

@pytest.fixture
def tile_coordinate_instance():
    return TileCoordinate()

def test_tile_coordinate_request(tile_coordinate_instance: TileCoordinate):
    tile_coordinate_instance.set_params(z=16,
                                        x=57999,
                                        y=39561,
                                        since="2015-07-01",
                                        until="2019-03-20",
                                        limit=1,
                                        offset=1,
                                        fields=['captureDate', 'firstPhotoTime', 'lastPhotoTime'],
                                        sort="id"
                                        )
    response = tile_coordinate_instance.call()

    assert response.status_code == 200
    assert response.ok == True

    assert response.json().get("limit") == 1
    assert response.json().get("offset") == 1