import sys
import ogr
from gdaltest import *

print "Got " + str(len(sys.argv)) + " arguments"
for i in sys.argv:
    print i

count_features()
