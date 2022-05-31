CC=gcc
CFLAGS=-g -m32 -g -Wall
RM=rm -f
TARGET=syracuse
OBJECTS=main.o syracuse_s_iter.o syracuse_s_rec.o

.PHONY: clean

.c.o:
	$(CC) $(CFLAGS) -c -o $@ $<

.s.o:
	$(CC) $(CFLAGS) -c -o $@ $<

all: syracuse

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	$(RM) *.o $(TARGET)
