from ..Config.App import app
from pynearmap.BaseRequest import BaseRequest

class Bounded(BaseRequest):

    base_uri = "staticmap"

    def __init__(self, server: int = 0):
        """

        Args:
            server: server domain rotation number. Valid numbers are 0-3.

        """
        super().__init__()
        self.base_url = "https://" + app.get("REGIONAL_CODE", "au") + str(server) + ".nearmap.com/"

    def set_params(self,
                   bbox: list,
                   zoom: int,
                   date: str,
                   ):
        """
        Retrieving an Image Centered on a Location

        Args:
            bbox:	Bounding box in the format [MIN LAT,MIN LON,MAX LAT,MAX LON]
                37.33197414633263,-122.0126095035584,
                37.33767824148404,-122.00526382713622

            zoom: Image zoom (web mercator zoom) eg. 18
            date: Date of the image, in the format YYYYMMDD

            When using the value "best" for zoom level, the system will generate the best image possible,
            in terms of pixels, for the specified location, up to a maximum of 6000 x 6000 pixels.
        """
        bbox = [str(value) for value in bbox]

        bbox_str = ",".join(bbox)

        self.queries = {
            "bbox": bbox_str,
            "zoom": str(zoom),
            "date": date,
            "httpauth": "false"
        }

        return self



