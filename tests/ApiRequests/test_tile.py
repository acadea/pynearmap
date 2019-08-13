import sys
from dotenv import load_dotenv
load_dotenv()
import os
sys.path.append(os.getenv("PATH_ROOT"))
import pytest
from PIL import Image
from io import BytesIO
from Pynearmap.Tile.Tile import Tile

@pytest.fixture
def tile_instance():
    return Tile()

def test_tile_request(tile_instance: Tile):
    tile_instance.set_params(tile_resource_type="Vert",
                             zoom_level=21,
                             x=1855981,
                             y=1265938,
                             format="jpg",
                             tertiary="satellite",
                             since="2015-08-13",
                             until="2019-03-26",
                             mosaic="latest",
                             )
    response = tile_instance.call()

    assert response.ok == True
    assert response.status_code == 200

    img = Image.open(BytesIO(response.content))

