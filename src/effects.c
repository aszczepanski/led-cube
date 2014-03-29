#include "effects.h"

#include <util/delay.h>
#include <stdlib.h>

#include "helpers.h"

void turn_on_and_off_each_layer(unsigned char direction) {
  int i, j;
  const double delay_time = 250000.0;
    
  switch (direction) {
  case BOTTOM_TOP:
    for (i=0; i<4; i++) {
      fill_cube(0x00);
      fill_layer(i, 0x0F);
      _delay_us(delay_time);
    }
    break;
  case TOP_BOTTOM:
    for (i=3; i>=0; i--) {
      fill_cube(0x00);
      fill_layer(i, 0x0F);
      _delay_us(delay_time);
    }
    break;
  case LEFT_RIGHT:
    for (i=0; i<4; i++) {
      fill_cube(0x00);
      for (j=0; j<4; j++) {
        fill_column(i, j);
      }
      _delay_us(delay_time);
    }
    break;
  case RIGHT_LEFT:
    for (i=3; i>=0; i--) {
      fill_cube(0x00);
      for (j=0; j<4; j++) {
        fill_column(i, j);
      }
      _delay_us(delay_time);
    }
    break;
  case FRONT_BACK:
    for (j=0; j<4; j++) {
      fill_cube(0x00);
      for (i=0; i<4; i++) {
        fill_column(i, j);
      }
      _delay_us(delay_time);
    }
    break;
  case BACK_FRONT:
    for (j=3; j>=0; j--) {
      fill_cube(0x00);
      for (i=0; i<4; i++) {
        fill_column(i, j);
      }
      _delay_us(delay_time);
    }
    break;
  }
}

static unsigned char rand_lower_than(unsigned char value) {
  return rand()%value;
}

void random_diodes(void) {
  int i;
  const int steps = 2000;
  const double delay_time = 2500;

  fill_cube(0x00);

  for (i=0; i<steps; i++) {
    set_diode(rand_lower_than(4), rand_lower_than(4),
      rand_lower_than(4), rand_lower_than(2));
    _delay_us(delay_time);
  }
}
