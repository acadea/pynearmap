from App.Config.App import app
from Src.BaseRequest import BaseRequest

class Centered(BaseRequest):

    base_uri = "staticmap"

    def __init__(self, server: int = 0):
        """

        Args:
            server: server domain rotation number. Valid numbers are 0-3.

        """
        super().__init__()
        self.base_url = "https://" + app.get("REGIONAL_CODE", "au") + str(server) + ".nearmap.com/"

    def set_params(self,
                   center: list,
                   size: str,
                   zoom: int,
                   date: str,
                   ):
        """
        Retrieving an Image Centered on a Location

        Args:
            center: Latitude and Longitude of the location on which to centre the image : eg. [37.334849,-122.008946]
            size: Size of the image in pixels eg 800x800
            zoom: Image zoom (web mercator zoom) eg. 18
            date: Date of the image, in the format YYYYMMDD
        """
        center = [str(value) for value in center]

        center_str = ",".join(center)

        self.queries = {
            "center": center_str,
            "size": size,
            "zoom": str(zoom),
            "date": date,
            "httpauth": "false"
        }

        return self



