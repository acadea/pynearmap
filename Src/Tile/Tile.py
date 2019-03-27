from Src.BaseRequest import BaseRequest

class Tile(BaseRequest):

    base_uri = "tiles/v3/"

    def set_params(self,
                   tile_resource_type: str,
                   zoom_level: int,
                   x: int,
                   y: int,
                   format: str,
                   tertiary: str = None,
                   since: str = None,
                   until: str = None,
                   mosaic: str = None
                   ):
        """

        Args:
            tile_resource_type:
                The resource type for the requested tiles. The available values are:

                Vert - for vertical imagery
                North - for North panorama imagery
                South - for South panorama imagery
                East - for East panorama imagery
                West - for West panorama imagery
                Note: the tileResourceType values are case sensitive.
            zoom_level:
                The zoom level. Uses the Google Maps Tile Coordinates.

                Note: the maximum zoom level is available from the Coverage API.
            x: The X tile coordinate (column). Uses the Google Maps Tile Coordinates.
            y: The Y tile coordinate (row). Uses the Google Maps Tile Coordinates.
            format:
                The format of the tile output.

                The available values are:

                jpg - always JPEG
                png - always PNG
                img - JPEG by default, PNG when the tile is partial
                Note that imagery is stored on Nearmap's servers as JPEG, so switching to PNG does not result in improvement in quality, however it will increase the size of the response.
            tertiary:
                The tertiary map to return when a Nearmap tile is not found.

                The available values are:

                none (default) - no tertiary imagery in the background
                satellite - use our current tertiary backdrop
                Note: returned tiles will always be blended with tiles from another survey. Tertiary tiles will only be blended when tertiary parameter is not 'none'.
            since:
                The first day from which to retrieve the tiles (inclusive).
                The two possible formats are:

                For a specific date: YYYY-MM-DD, e.g. 2015-10-31 to retrieve imagery since this date.
                For a relative date: xxY, xxM, or xxD, e.g. 5M to retrieve imagery since 5 months ago.
                Notes:

                If specified, the since parameter controls the earliest imagery that is returned. If there are multiple captures after the date specified by the since parameter, the latest imagery is returned.

                If the mosaic parameter is set to earliest, the imagery on or after the date specified by the since parameter is returned.

                If neither since nor until are specified, the request returns the latest imagery.
            until:
                The last day from which to retrieve the tiles (inclusive).

                The two possible formats are:

                For a specific date: YYYY-MM-DD, e.g. 2015-10-31 to retrieve imagery until this date.
                For a relative date: xxY, xxM, or xxD, e.g. 5M to retrieve imagery until 5 months ago.
                Notes:

                If specified, and imagery at that location at that date exists, the request returns the imagery.
                If specified, and imagery at that location at that date does not exist, the request returns imagery of the next available date before the specified date.
                If neither since nor until are specified, the request returns the latest imagery.
            mosaic:
                Specifies the order in which the surveys covering the specified area are prioritised.

                The available values are:

                latest - the imagery with the later capture date is prioritised

                earliest - imagery with the earlier capture date is prioritised

                If the mosaic parameter is not specified, the imagery with the later capture date is prioritised.

                To return imagery on or after a specified date, use mosaic=earliest in combination with the since parameter.
        """
        separator = "/"

        uri = separator.join([tile_resource_type, str(zoom_level), str(x), str(y)]) + "." + format

        self.set_uri(uri)

        self.queries = {
            "tertiary": tertiary,
            "since": since,
            "until": until,
            "mosaic": mosaic
        }

        return self


if __name__ == '__main__':
    tile_instance = Tile()
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

    a = 12