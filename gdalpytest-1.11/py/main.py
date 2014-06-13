import sys
import ogr

ds = ogr.Open("Township.shp")

if ds is None:
	print "Open failed.\n"
	sys.exit(1)

lyr = ds.GetLayerByName("Township")
lyr.ResetReading()

for feat in lyr:
	print "I found a feature!"
