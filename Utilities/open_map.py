import geopandas as gdp
import json 
import sys
sys.path.append('../')
import ENVIRONMENT_VARIABLES as EV 

def mesh_map():
    shape = gdp.read_file(EV.MESH)
    shape = shape.to_crs(epsg=4326)
        
    shape_json = json.loads(shape.to_json())
    return shape_json, shape

