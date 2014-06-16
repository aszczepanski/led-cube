#include "helpers.h"

extern volatile uint8_t tab[8][8];

void fill_layer(uint8_t layer, uint8_t value) {
  int i;
  if (layer < 8) {
    for (i=0; i<8; i++) {
      tab[layer][i] = value;
    }
  }
}

void fill_column(uint8_t x, uint8_t y) {
  int i;
  for (i=0; i<8; i++) {
    set_voxel(x, y, i, 1);
  }
}

void fill_cube(uint8_t value) {
  int i;
  for (i=0; i<8; i++) {
    fill_layer(i, value);
  }
}

void set_voxel(uint8_t x, uint8_t y, uint8_t z, uint8_t value) {
  volatile unsigned char* ptr = &tab[z][y];
  if (value == 0) {
    *ptr &= ~(1<<x);
  } else {
    *ptr |= (1<<x);
  }
}

int get_voxel(uint8_t x, uint8_t y, uint8_t z) {
  return tab[z][y] & (1<<x);
}

void shift(uint8_t axis) {
  int x,y,z;
  for (x=0; x<8; x++) {
    for (y=0; y<8; y++) {
      if (get_voxel(x,y,0)) {
        set_voxel(x,y,0,0);
      }
      for (z=1; z<8; z++) {
        if (get_voxel(x,y,z)) {
          set_voxel(x,y,z-1,1);
          set_voxel(x,y,z,0);
        }
      }
    }
  }
}
