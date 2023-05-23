import sys
sys.path.append('../')
from Utilities.open_map import mesh_map


        # shape = shape.drop('LOCI_URI21', axis=1)
        # shape = shape.drop('AUS_NAME21', axis=1)
        # shape = shape.drop('AUS_CODE21', axis=1)
        # shape = shape.drop('SA2_CODE21', axis=1)
        # shape = shape.drop('SA1_CODE21', axis=1)
        # shape = shape.drop('CHG_LBL21', axis=1)
        # shape = shape.drop('STE_NAME21', axis=1)
        # shape = shape.drop('CHG_FLAG21', axis=1)

shape_json, filtered_shape = mesh_map(True, pre_filtered=False) 
f = open("mesh_centres.txt", "w", encoding="utf-8")
f.write('MB Code\tLatitude\tLongitude\n')

geos = filtered_shape['geometry']
names = filtered_shape['MB_CODE21']

for geo, name in zip(geos, names):
    try:
        centroid = geo.centroid 
        lat = centroid.x
        lon = centroid.y
        f.write(f"{name}\t{lat}\t{lon}+\n")
    except Exception as ex:
        print(ex)
    