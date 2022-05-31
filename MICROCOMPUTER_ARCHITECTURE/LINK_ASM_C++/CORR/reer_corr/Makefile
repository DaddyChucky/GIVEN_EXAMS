CXX=g++
CFLAGS=-g -m32 -Wall
LDFLAGS=-lm
RM=rm -f
TARGET=reer
OBJECTS=main.o reer.o compte.o salaireFinalAsm.s montantAEpargnerChaqueAnneeAsm.s montantAInvestirMaintenantAsm.s montantAmasseFinalAvantRetraiteAsm.s montantInvestirMaintenantCompteAsm.s

.PHONY: clean

.cpp.o:
	$(CXX) $(CFLAGS) -c -o $@ $<

all: reer

$(TARGET): $(OBJECTS)
	$(CXX) $(CFLAGS) $(LDFLAGS) -o $@ $^

clean:
	$(RM) *.o $(TARGET) 
