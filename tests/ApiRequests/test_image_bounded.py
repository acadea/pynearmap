import sys
from dotenv import load_dotenv
load_dotenv()
import os
sys.path.append(os.getenv("PATH_ROOT"))
import pytest
from PIL import Image
from io import BytesIO
from Pynearmap.Image.Bounded import Bounded

@pytest.fixture
def image_bounded_instance():
    return Bounded()

def test_image_bounded_request(image_bounded_instance: Bounded):
    image_bounded_instance.set_params(bbox=[37.33197414633263,-122.0126095035584,
                                            37.33767824148404,-122.00526382713622
                                            ],
                                       zoom=18,
                                       date="20150314",
                                       )
    response = image_bounded_instance.call()

    assert response.status_code == 200
    assert response.ok == True

    img = Image.open(BytesIO(response.content))
