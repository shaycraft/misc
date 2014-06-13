LIBS = -lgdal -lcurl -lz -lpthread -ldl -lgeos_c  -lsqlite3 -lexpat -lxerces-c -lpthread -lgif -ljpeg -lpng -lxml2 -lpq -lpcre
OBJS = cgdaltest.o
EXE = cgdaltest
GCC = g++
ARGS = -Wall

$(EXE): $(OBJS) 
	$(GCC) $(ARGS) -o $(EXE) $(OBJS) $(LIBS)

cgdaltext.o: cgdaltext.c
	$(GCC) $(ARGS) -c cgdaltest.c

clean:
	rm -f $(EXE) $(OBJS)
