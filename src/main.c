#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#include <stdint.h>

#include "usart.h"
#include "helpers.h"
#include "effects.h"

volatile uint8_t tab[8][8];

ISR(TIMER2_COMP_vect);
static inline void init_timer(void);
static inline void init_io(void);

int main(void) {
	init_timer();
  init_io();

  USART_Init();

  sei();

  fill_cube(0xFF);

  _delay_us(1500000);

  int mode = (PIND & (1<<PD3));  

  if (mode) {

    while (1) {

      random_filler(1);
      random_filler(0);
      loadbar();
      rain(100);

      send_voxels_rand_z(200);

      set_edges();
      _delay_us(5000000);
    }

  } else {

    int escape = 0;
    int counter = 0;

    while (1) {

      uint8_t byte;
      byte = USART_Receive();

      if (!escape) {
        if (byte == 0xAB) { // escape character
          escape = 1;
        } else if (counter < 64) {
          tab[counter/8][counter%8] = byte;
          counter++;
        }
      } else {
        if (byte == 0xCD) { // start character
          counter = 0;
        } else if (byte == 0xAB && counter < 64) {
          tab[counter/8][counter%8] = byte;
          counter++;
        }
        escape = 0;
      }
    }

  }
  return 0;
}

ISR(TIMER2_COMP_vect) {
  int i;
  static uint8_t current_layer = 0;

  // PORT A = data bus
  // PORT B = address bus (74HC138)
  // char tab[8] holds 64 bits of data for the latch array

  PORTC = 0x00;

  PORTB = 0x08; // OE set high

  for (i=0; i<8; i++) {
    PORTA = tab[current_layer][i];
    // PORTB = 0x08; // OE set high
    // PORTB |= i+1;
    PORTB = 0x08 | (i+1);
  }

  PORTB &= ~0x08;

  PORTC = (1 << current_layer);

  if (++current_layer > 7) {
    current_layer = 0;
  }
}

static inline void init_timer(void) {
  OCR2 = 10;
  TCCR2 |= (1 << CS20) | (1 << CS22);
  TCCR2 |= (1 << WGM21);
  TCNT2 = 0x00;
  TIMSK |= (1 << OCIE2);
}

static inline void init_io(void) {
  DDRA = 0xFF;
  DDRB = 0xFF;
  DDRC = 0xFF;
  DDRD = 0xF7;

  PORTA = 0x00;
  PORTB = 0x00;
  PORTC = 0x00;
  PORTD = 0x48;
}

