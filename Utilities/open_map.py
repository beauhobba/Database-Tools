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


def poa_map():
    shape = gdp.read_file(EV.POST)
    shape = shape.to_crs(epsg=4326)
        
    shape_json = json.loads(shape.to_json())
    return shape_json, shape


def regular_map():
    lga_gdf = gdp.read_file(f"{EV.REGULAR}")
    lga_gdf = lga_gdf[lga_gdf['STE_NAME16']=='New South Wales']
    lga_gdf['LGA_CODE20'] = lga_gdf['LGA_CODE20'].astype(str)
    df_map = lga_gdf[['LGA_CODE20', 'geometry', 'LGA_NAME20']]

    df_map = df_map.to_crs(epsg=4326) # convert the coordinate reference system to lat/long
    lga_json = df_map.__geo_interface__
    return lga_json, df_map
    


def sa2_map():
    shape = gdp.read_file(EV.SA2)
    shape = shape.to_crs(epsg=4326)
        
    shape_json = json.loads(shape.to_json())
    return shape_json, shape


def sa3_map():
    shape = gdp.read_file(EV.SA3)
    shape = shape.to_crs(epsg=4326)
        
    shape_json = json.loads(shape.to_json())
    return shape_json, shape


def sa4_map():
    shape = gdp.read_file(EV.SA4)
    shape = shape.to_crs(epsg=4326)
        
    shape_json = json.loads(shape.to_json())
    return shape_json, shape


def sa1_map():
    shape = gdp.read_file(EV.SA1)
    shape = shape.to_crs(epsg=4326)
        
    shape_json = json.loads(shape.to_json())
    return shape_json, shape


def lga_map():
    shape = gdp.read_file(EV.LGA)
    shape = shape.to_crs(epsg=4326)
        
    shape_json = json.loads(shape.to_json())
    return shape_json, shape



def remoteness_map():
    shape = gdp.read_file(EV.LGA)
    shape = shape.to_crs(epsg=4326)
        
    shape_json = json.loads(shape.to_json())
    return shape_json, shape

def custom_map(name):
    shape = gdp.read_file(name)
    shape = shape.to_crs(epsg=4326)
        
    shape_json = json.loads(shape.to_json())
    return shape_json, shape