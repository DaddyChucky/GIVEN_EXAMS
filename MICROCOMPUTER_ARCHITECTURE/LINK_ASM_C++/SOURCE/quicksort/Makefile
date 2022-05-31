CC=gcc
CFLAGS=-g -m32 -g -Wall
RM=rm -f
TARGET=quicksort
OBJECTS=main.o quicksort_s.o

.PHONY: clean

.c.o:
	$(CC) $(CFLAGS) -c -o $@ $<

.s.o:
	$(CC) $(CFLAGS) -c -o $@ $<

all: quicksort

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	$(RM) *.o $(TARGET)
