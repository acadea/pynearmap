from Pynearmap.BaseRequest import BaseRequest

class Polygon(BaseRequest):
    base_uri = "coverage/v2/poly/"

    def set_params(self,
                   polygon: list,
                   since: str = None,
                   until: str = None,
                   limit: int = None,
                   offset: int = None,
                   fields: list = None,
                   sort: str = None
                   ):
        """
        This API retrieves coverage (surveys) for a given polygon.
        Args:
            polygon (list):
                The polygon for which the surveys are retrieved. The polygon is depicted by a set of
                LONG,LAT points, where the first and the last points must be the same.

                For example:

                138.59707796614592,-34.91729448760797

                138.61703360121672,-34.91729448760797

                138.61703360121672,-34.927709974005474

                138.59707796614592,-34.927709974005474

                138.59707796614592,-34.91729448760797
                Notes-
                    The API returns all surveys partially intersecting the requested polygon.
                    The LONG comes before the LAT

            since (str):
                The first day from which to retrieve the surveys (inclusive).

                The two possible formats are:

                For a specific date: YYYY-MM-DD, e.g. 2015-10-31 to retrieve surveys since this date.
                For a relative date: xxY, xxM, or xxD, e.g. 5M to retrieve surveys since 5 months ago.
                The since and until parameters are used to further restrict the surveys that are returned.
            until:

                The last day from which to retrieve the surveys (inclusive).

                The two possible formats are:

                For a specific date: YYYY-MM-DD, e.g. 2015-10-31 to retrieve surveys until this date.
                For a relative date: xxY, xxM, or xxD, e.g. 5M to retrieve surveys until 5 months ago.
                The since and until parameters are used to further restrict the surveys that are returned.

            limit: The limit of the total number of surveys returned. The default value is 20. The surveys
                are returned from the most recent to the least recent survey.

            offset: The offset of the first survey to be displayed. With no offset, the first survey to be displayed is
                the most recent one. If the offset is 3 for example, the first survey to be displayed is the 4th recent
                one.

            fields:This is a comma-separated list of field names that will appear in the response.

                The id field will always be among the returned fields, even if not specified.

                If this parameter is not used in the URL request, then all the fields are returned.

                The available values are:

                captureDate
                firstPhotoTime
                id
                lastPhotoTime
                location
                onlineTime
                pixelSize
                resources
                timezone
                utcOffset
                Note: the fields values are case sensitive.

            sort:
                The field by which to sort the surveys.

                Only one field can be specified.

                If this parameter is not used in the URL request, then the surveys are sorted by captureDate in descending order.

                To sort in ascending order, pass the field name, e.g sort=lastPhotoTime. This will sort the surveys
                according to the lastPhotoTime from earliest to latest.

                To sort in descending order, pass the field name with the "-" prefix, e.g. sort=-pixelSize. This will sort the surveys according to the pixelSize from the largest to the smallest.

                If you sort by location, the following are the precedence rules for comparing location objects:

                country
                state
                region
                For example, "NZ, MWT, PalmerstonNorth" will come after "AU, NSW, Williamstown" if sorted in ascending order.

                The available values are:

                captureDate
                firstPhotoTime
                id
                lastPhotoTime
                location
                onlineTime
                pixelSize
                timezone
                utcOffset
        """
        separator = ","
        polygon = [str(value) for value in polygon]
        polygon_string = separator.join(polygon)
        self.queries = {
            "since": since,
            "until": until,
            "limit" : limit,
            "offset" : offset,
            "fields" : separator.join(fields) if fields is not None else None,
            "sort" : sort
        }
        self.set_uri(polygon_string)
        return self

if __name__ == '__main__': # testing
    nearmap = Polygon()
    polygon = [138.59707796614592, -34.91729448760797,
                138.61703360121672, -34.91729448760797,
                138.61703360121672, -34.927709974005474,
                138.59707796614592, -34.927709974005474,
                138.59707796614592, -34.91729448760797]
    nearmap.set_params(polygon=polygon)
    response = nearmap.call()
    a = 12