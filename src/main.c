#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#include <stdint.h>

#include "usart.h"
#include "helpers.h"
#include "effects.h"

volatile uint8_t tab[4][4];

ISR(TIMER0_COMP_vect);
static inline void init_timer(void);
static inline void init_io(void);

int main(void) {

	init_timer();
  init_io();

  USART_Init();

  sei();

  fill_cube(0x0F);

  _delay_us(1000000);

  uint8_t counter = 0;

  while (1) {

    uint8_t byte;
    byte = USART_Receive();
    
    if (byte == 0xAB) {
      counter = 0;
    } else if (counter < 16) {
      tab[counter/4][counter%4] = byte;
      counter++;
    }

/*
    turn_on_and_off_each_layer(BOTTOM_TOP);
    turn_on_and_off_each_layer(LEFT_RIGHT);
    turn_on_and_off_each_layer(FRONT_BACK);
    turn_on_and_off_each_layer(TOP_BOTTOM);
    turn_on_and_off_each_layer(RIGHT_LEFT);
    turn_on_and_off_each_layer(BACK_FRONT);

    random_diodes();
*/
  }

	return 0;
}

ISR(TIMER0_COMP_vect) {
  static uint8_t current_layer = 0;

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

static inline void init_timer(void) {
	TCCR0=(1<<WGM01)|(1<<CS01)|(1<CS00);
	OCR0 = 156;
	TIMSK |= (1<<OCIE0);
}

static inline void init_io(void) {
  DDRA = 0xFF;
  DDRB = 0xFF;
  DDRC = 0xFF;
  DDRD = 0xFF;
  PORTD |= (1<<PD7);
}

