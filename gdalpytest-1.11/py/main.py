import sys
import ogr
import tkFileDialog
from gdaltest import *

print "Got " + str(len(sys.argv)) + " arguments"
for i in sys.argv:
    print type(i) 
    print i

print sys.argv[1]

# this is a file dialog
tkFileName = tkFileDialog.askopenfilename()
print "You selected " + tkFileName

count_features(sys.argv[1])
