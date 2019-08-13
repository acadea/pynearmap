# Nearmap-py
Lightweight Nearmap API client implemented in pure Python. Read the API documentation at https://docs.nearmap.com/

# Getting Started

```python
pip install pynearmap
```

## API Credentials

You can either pass your nearmap api key directly to the constructor:

```python
from pynearmap.Tile import Tile

api_key = "*****"

tile_client = Tile(api_key=api_key)

# ---

```

Otherwise create a new environmental variable "NEARMAP_KEY" in project root

### Environmental Variable
Copy the keys in .env-example to your project's .env file

"NEARMAP_KEY"  -- api key

"NEARMAP_BASE_URL"  -- eg https://api.nearmap.com/

"REGIONAL_CODE" -- eg au


# Requirement
dotenv

pytest

Pillow




# Usage

### Coverage

##### Point
```python
point = Point()

point.set_params(point=[138.59707796614592,-34.91729448760797],
                 since="2015-07-01",
                 until="2019-03-20",
                 limit=1,
                 offset=1,
                 fields=['captureDate', 'firstPhotoTime', 'lastPhotoTime'],
                 sort="id"
                 )
response = point.call()
```

##### TileCoordinate
```python
tile_coordinate_instance = TileCoordinate()
tile_coordinate_instance.set_params(z=16,
                                    x=57999,
                                    y=39561,
                                    since="2015-07-01",
                                    until="2019-03-20",
                                    limit=1,
                                    offset=1,
                                    fields=['captureDate', 'firstPhotoTime', 'lastPhotoTime'],
                                    sort="id"
                                    )
response = tile_coordinate_instance.call()
```

##### Polygon
 
```python
polygon_instance = Polygon()
polygon_coord = [138.59707796614592, -34.91729448760797,
               138.61703360121672, -34.91729448760797,
               138.61703360121672, -34.927709974005474,
               138.59707796614592, -34.927709974005474,
               138.59707796614592, -34.91729448760797]
polygon_instance.set_params(polygon=polygon_coord,
                   since="2015-07-01",
                   until="2019-03-20",
                   limit=1,
                   offset=1,
                   fields=['captureDate', 'firstPhotoTime', 'lastPhotoTime'],
                   sort="id"
                   )
response = polygon_instance.call()

```


### Image

##### Bounded
```python
image_bounded_instance = Bounded()
image_bounded_instance.set_params(bbox=[37.33197414633263,-122.0126095035584,
                                        37.33767824148404,-122.00526382713622
                                        ],
                                   zoom=18,
                                   date="20150314",
                                   )
    response = image_bounded_instance.call()

```


##### Centered
```python
image_centered_instance = Centered()
image_centered_instance.set_params(center=[37.334849,-122.008946],
                                   size="800x800",
                                   zoom=18,
                                   date="20150314",
                                   )
response = image_centered_instance.call()

```


### Tile

##### Default Tile
```python
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
```

##### Specified Survey
```python
tile_specified_instance = SpecifiedSurvey()
tile_specified_instance.set_params(surveyid="100-4c51ffe8-ab52-11e8-9b7a-b3f8ca0bcb81",
                                       content_type="Vert",
                                       zoom_level=16,
                                       x=57999,
                                       y=39561,
                                       format="jpg")

response = tile_specified_instance.call()
```
