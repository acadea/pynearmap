import sys
from dotenv import load_dotenv
load_dotenv()
import os
sys.path.append(os.getenv("PATH_ROOT"))
import pytest
from PIL import Image
from io import BytesIO
from Pynearmap.Tile.SpecifiedSurvey import SpecifiedSurvey

@pytest.fixture
def tile_specified_instance():
    return SpecifiedSurvey()

def test_tile_specified_survey_request(tile_specified_instance: SpecifiedSurvey):

    tile_specified_instance.set_params(surveyid="100-4c51ffe8-ab52-11e8-9b7a-b3f8ca0bcb81",
                                       content_type="Vert",
                                       zoom_level=16,
                                       x=57999,
                                       y=39561,
                                       format="jpg")

    response = tile_specified_instance.call()

    assert response.status_code == 200
    assert response.ok == True

    img = Image.open(BytesIO(response.content))



