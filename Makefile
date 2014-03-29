CC = avr-gcc
LD = avr-gcc
CFLAGS = -Wall -Os
LDFLAGS = -Wall -Os

OBJ_CPY = avr-objcopy
IHEX = ihex
EEPROM = .eeprom

SRCS = main.c helpers.c effects.c
OBJS=$(addprefix ./obj/, $(addsuffix .o, $(SRCS)))

LFUSE = 0xe4
HFUSE = 0xd9

#  default:
# LFUSE = 0xe1
# HFUSE = 0x99

DEVICE = atmega16
CLOCK = 8000000
PROGRAMMER = usbasp
HEX = prog.hex
TARGET = a.out

AVRDUDE = sudo avrdude -p $(DEVICE) -c $(PROGRAMMER)

FLA: $(HEX)
	$(AVRDUDE) -U flash:w:$(HEX)

$(HEX): $(TARGET)
	$(OBJ_CPY) -O $(IHEX) -R $(EEPROM) $(TARGET) $(HEX)

$(TARGET): $(OBJS)
	$(LD) -o $(TARGET) $(OBJS) $(LDFLAGS) -DF_CPU=$(CLOCK) -mmcu=$(DEVICE)
./obj/%.c.o: ./src/%.c
	-mkdir -p obj
	$(CC) -c $< -o $@ $(CFLAGS) -DF_CPU=$(CLOCK) -mmcu=$(DEVICE)

fusew:
	$(AVRDUDE) -U hfuse:w:$(HFUSE):m -U lfuse:w:$(LFUSE):m
fuser:
	$(AVRDUDE) -U hfuse:r:-:h -U lfuse:r:-:h

.PHONY: clean

clean:
	-rm -rf $(TARGET) $(HEX) obj/
