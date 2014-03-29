#include "helpers.h"

extern volatile unsigned char tab[4][4];

void fill_layer(unsigned char layer, unsigned char value) {
  int i;
  if (layer < 4) {
    for (i=0; i<4; i++) {
      tab[layer][i] = value;
    }
  }
}

void fill_column(unsigned char x, unsigned char y) {
  int i;
  for (i=0; i<4; i++) {
    set_diode(x, y, i, 1);
  }
}

void fill_cube(unsigned char value) {
  int i;
  for (i=0; i<4; i++) {
    fill_layer(i, value);
  }
}

void set_diode(unsigned char x, unsigned char y, unsigned char z, unsigned char value) {
  volatile unsigned char* ptr = &tab[z][y];
  if (value == 0) {
    *ptr &= ~(1<<x);
  } else {
    *ptr |= (1<<x);
  }
}
