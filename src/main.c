#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#include "helpers.h"
#include "effects.h"

volatile unsigned char tab[4][4];

volatile unsigned char current_layer = 0;

ISR(TIMER0_COMP_vect) {

  PORTB &= 0xF0;

  PORTA = 0x00;
  PORTA |= (tab[current_layer][2] & 0x01) << PA7;
  PORTA |= (((tab[current_layer][2] & 0x02) >> 1) << PA6);
  PORTA |= (((tab[current_layer][2] & 0x04) >> 2) << PA5);
  PORTA |= (((tab[current_layer][2] & 0x08) >> 3) << PA4);
  PORTA |= (tab[current_layer][3] & 0x01) << PA3;
  PORTA |= (((tab[current_layer][3] & 0x02) >> 1) << PA2);
  PORTA |= (((tab[current_layer][3] & 0x04) >> 2) << PA1);
  PORTA |= (((tab[current_layer][3] & 0x08) >> 3) << PA0);

  PORTC = tab[current_layer][1] << 4;
  PORTC |= tab[current_layer][0];

  PORTB = (1 << current_layer);

  if (++current_layer > 3) {
    current_layer = 0;
  }
}

static inline void init_timer() {
	TCCR0=(1<<WGM01)|(1<<CS01)|(1<CS00);
	OCR0 = 156;
	TIMSK |= (1<<OCIE0);
}

static inline void init_io() {
  DDRA = 0xFF;
  DDRB = 0xFF;
  DDRC = 0xFF;
  DDRD = 0xFF;
  PORTD |= (1<<PD7);
}

int main(void) {

  int i, j, k;

	init_timer();
  init_io();


  PORTA |= (1<<PA0);
  PORTA |= (1<<PA1);
  PORTA |= (1<<PA2);
  PORTA |= (1<<PA3);

  PORTA |= (1<<PA4);
  PORTA |= (1<<PA5);
  PORTA |= (1<<PA6);
  PORTA |= (1<<PA7);

  PORTC |= (1<<PC0);
  PORTC |= (1<<PC1);
  PORTC |= (1<<PC2);
  PORTC |= (1<<PC3);

  PORTC |= (1<<PC4);
  PORTC |= (1<<PC5);
  PORTC |= (1<<PC6);
  PORTC |= (1<<PC7);

  PORTB |= (1<<PB0);
  PORTB |= (1<<PB1);
  PORTB |= (1<<PB2);
  PORTB |= (1<<PB3);

  _delay_us(1000000u);

  PORTB = 0x00;
  PORTA = 0x00;
  PORTC = 0x00;

  sei();

  while (1) {
    for (i=0; i<4; i++) {
      for (k=0; k<4; k++) {
        for (j=0; j<4; j++) {
          tab[k][j] = 0x00;
        }
      }
      for (j=0; j<4; j++) {
        tab[i][j] = 0x0F;
      }
      _delay_us(250000u);
    }
   
    for (i=0; i<4; i++) {
      for (k=0; k<4; k++) {
        for (j=0; j<4; j++) {
          tab[k][j] = 0x00;
        }
      }
      for (j=0; j<4; j++) {
        tab[j][i] = 0x0F;
      }
      _delay_us(250000u);
    }

    for (i=0; i<4; i++) {
      for (k=0; k<4; k++) {
        for (j=0; j<4; j++) {
          tab[k][j] = 0x00;
        }
      }
      for (j=0; j<4; j++) {
        for (k=0; k<4; k++) {
          tab[j][k] = 1<<i;
        }
      }
      _delay_us(250000u);
    }

  }

	return 0;
}
