import sys
from dotenv import load_dotenv
load_dotenv()
import os
sys.path.append(os.getenv("PATH_ROOT"))
import pytest
from PIL import Image
from io import BytesIO
from pynearmap.Image.Centered import Centered

@pytest.fixture
def image_centered_instance():
    return Centered()

def test_image_centered_request(image_centered_instance: Centered):
    image_centered_instance.set_params(center=[37.334849,-122.008946],
                                       size="800x800",
                                       zoom=18,
                                       date="20150314",
                                       )
    response = image_centered_instance.call()

    assert response.status_code == 200
    assert response.ok == True

    img = Image.open(BytesIO(response.content))
