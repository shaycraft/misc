import sys
import ogr

def count_features(filename):
    ds = ogr.Open(filename)

    if ds is None:
        print "Open failed.\n"
        sys.exit(1)

    lyr = ds.GetLayerByName("WELLS")
    lyr.ResetReading()

    n = 0
    for feat in lyr:
        n=n+1
        fieldcount = feat.GetGeomFieldCount()

    print "fieldcount = " + str(fieldcount)

    print "Found " + str(n) + " features"
