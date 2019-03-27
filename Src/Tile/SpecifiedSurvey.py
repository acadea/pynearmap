from Src.BaseRequest import BaseRequest

class SpecifiedSurvey(BaseRequest):
    base_uri = "tiles/v3/surveys/"

    def set_params(self,
                   surveyid: str,
                   content_type: str,
                   zoom_level: int,
                   x: int,
                   y: int,
                   format: str
                   ):
        """

        Args:
            surveyid:
                The survey ID in the format of UUID. Only tiles of the specified survey will be returned.
                You can use the ID from the survey object returned by the Coverage API.

            content_type: The content type for the requested tiles. The available values are:
                Vert - for vertical imagery
                North - for North panorama imagery
                South - for South panorama imagery
                East - for East panorama imagery
                West - for West panorama imagery
                Note: the tileResourceType values are case sensitive.
            zoom_level: The zoom level. The highest resolution is typically 21. Uses the Google Maps Tile Coordinates.
            x: The X tile coordinate (column). Uses the Google Maps Tile Coordinates.
            y: The Y tile coordinate (row). Uses the Google Maps Tile Coordinates.
            format:
                The format of the tile output. The available values are:

                jpg - always JPEG
                png - always PNG
                img - JPEG by default, PNG when the tile is partial
                Note that imagery is stored on Nearmap's servers as JPEG, so switching to PNG does not result in improvement in quality, however it will increase the size of the response.
        """
        seperator = "/"
        uri = seperator.join([surveyid, content_type, str(zoom_level), str(x), str(y)]) + "." + format
        self.set_uri(uri)
        return self


if __name__ == '__main__':
    from Src.Coverage.Point import Point

    tile_specified_instance = SpecifiedSurvey()
    # coverage_point_instance = Point()
    #
    # point = [138.59707796614592, -34.91729448760797]
    # coverage_point_instance.set_params(point=point)
    # response = coverage_point_instance.call()
    #
    # survey = response.json()

    tile_specified_instance.set_params(surveyid="100-4c51ffe8-ab52-11e8-9b7a-b3f8ca0bcb81",
                                       content_type="Vert",
                                       zoom_level=16,
                                       x=57999,
                                       y=39561,
                                       format="jpg")
    response = tile_specified_instance.call()

    a = 12