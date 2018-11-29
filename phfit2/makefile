CC=ifort
# CC=gfortran
CFLAGS=-fPIC -O3
SONAME=libphfit2.so
MODULES=phfit2.f phfit2_wrappers.f90
SOURCES=$(MODULES)
TMP=$(MODULES:.f=.o)
OBJECTS=$(TMP:.f90=.o)
RM=@-rm

LIBDIR=../pyphfit2/lib
$(shell mkdir -p $(LIBDIR) >/dev/null)

all: $(SONAME)

phfit2_wrapper.o: phfit2.o

install:
	@echo "# copying $(SONAME)"
	$(shell cp ./$(SONAME) $(LIBDIR))

$(SONAME): $(OBJECTS)
	@echo "# linking"
	$(CC) -shared -Wl,-soname,$(SONAME) -o $(SONAME) $(OBJECTS) -lc

$(OBJECTS): makefile

%.o: %.f
	@echo "# compiling $*.f"
	$(CC) $(CFLAGS) -c  -o $@ $<

%.o: %.f90
	@echo "# compiling $*.f90"
	$(CC) $(CFLAGS) -c -o $@ $<

.PHONY: clean uninstall

clean:
	$(RM) *.o *.mod *~ $(SONAME) 2> /dev/null; true

uninstall:
	$(RM) $(LIBDIR)/$(SONAME) 2> /dev/null; true
