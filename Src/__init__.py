from Src.Coverage.Point import Point
from Src.Coverage.Polygon import Polygon
from Src.Coverage.TileCoordinate import TileCoordinate

from Src.Image.Bounded import Bounded
from Src.Image.Centered import Centered

from Src.Tile.Tile import Tile as StandardTile
from Src.Tile.SpecifiedSurvey import SpecifiedSurvey

class CoveragePoint(Point):
    pass

class CoveragePolygon(Polygon):
    pass

class CoverageTileCoordinate(TileCoordinate):
    pass

class ImageBounded(Bounded):
    pass

class ImageCentered(Centered):
    pass

class Tile(StandardTile):
    pass

class TileSpecifiedSurvey(SpecifiedSurvey):
    pass