import geopandas
from geopandas.tools import sjoin

# A list of points to check. Using Boulder trailheads for now
point = geopandas.GeoDataFrame.from_file('shapefiles/Trailheads.shp') 
# A map of all Boulder County Open Space
poly  = geopandas.GeoDataFrame.from_file('shapefiles/County_Open_Space.shp')

pointInPolys = sjoin(point, poly, how='left')

grouped = pointInPolys.groupby('index_right')

list(grouped)