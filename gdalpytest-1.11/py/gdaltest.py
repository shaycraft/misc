import sys
import ogr

def count_features():
	ds = ogr.Open("../WELLS.SHP")

	if ds is None:
		print "Open failed.\n"
		sys.exit(1)

	lyr = ds.GetLayerByName("WELLS")
	lyr.ResetReading()

	n = 0
	for feat in lyr:
		n=n+1

	print "Found " + str(n) + " features"
