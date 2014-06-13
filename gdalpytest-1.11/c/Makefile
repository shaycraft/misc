LIBS = -lgdal -lcurl -lz -lpthread -ldl -lgeos_c  -lsqlite3 -lexpat -lxerces-c -lpthread -lgif -ljpeg -lpng -lxml2 -lpq -lpcre -lstdc++ -lm
OBJS = cgdaltest.o
EXE = cgdaltest
GCC = gcc
ARGS = -Wall

$(EXE): $(OBJS) 
	$(GCC) $(ARGS) -o $(EXE) $(OBJS) $(LIBS)

cgdaltest.o: cgdaltest.c
	$(GCC) $(ARGS) -c cgdaltest.c

clean:
	rm -f $(EXE) $(OBJS)
