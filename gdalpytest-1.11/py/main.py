import sys
import ogr
from gdaltest import *

print "Got " + str(len(sys.argv)) + " arguments"
for i in sys.argv:
    print type(i) 
    print i

print sys.argv[1]

count_features(sys.argv[1])
