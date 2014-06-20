import sys
from osgeo import gdal

ds = gdal.OpenEx('../WELLS.SHP', gdal.OF_VECTOR)
if ds is None:
    print "Open failed.\n";
    sys.exit(1);

lyr = ds.GetLayerByName ("WELLS")
count= 0
for feat in lyr:
    count = count + 1


print "Found {0} features".format(count)