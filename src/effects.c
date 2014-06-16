#include "effects.h"

#include <util/delay.h>
#include <stdlib.h>

#include "helpers.h"

void launch_effect(int effect) {
  switch (effect) {
  case 0:
    rain(100);
    break;
  case 1:
    break;
  case 2:
    random_filler(1);
    random_filler(0);
    break;
  }
}

void turn_on_and_off_each_layer(unsigned char direction) {
  int i, j;
  const double delay_time = 250000.0;
    
  switch (direction) {
  case BOTTOM_TOP:
    for (i=0; i<8; i++) {
      fill_cube(0x00);
      fill_layer(i, 0x0F);
      _delay_us(delay_time);
    }
    break;
  case TOP_BOTTOM:
    for (i=7; i>=0; i--) {
      fill_cube(0x00);
      fill_layer(i, 0x0F);
      _delay_us(delay_time);
    }
    break;
  case LEFT_RIGHT:
    for (i=0; i<8; i++) {
      fill_cube(0x00);
      for (j=0; j<8; j++) {
        fill_column(i, j);
      }
      _delay_us(delay_time);
    }
    break;
  case RIGHT_LEFT:
    for (i=7; i>=0; i--) {
      fill_cube(0x00);
      for (j=0; j<8; j++) {
        fill_column(i, j);
      }
      _delay_us(delay_time);
    }
    break;
  case FRONT_BACK:
    for (j=0; j<8; j++) {
      fill_cube(0x00);
      for (i=0; i<8; i++) {
        fill_column(i, j);
      }
      _delay_us(delay_time);
    }
    break;
  case BACK_FRONT:
    for (j=7; j>=0; j--) {
      fill_cube(0x00);
      for (i=0; i<8; i++) {
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
    set_voxel(rand_lower_than(8), rand_lower_than(8),
      rand_lower_than(8), rand_lower_than(2));
    _delay_us(delay_time);
  }
}

void set_edges(void) {
  int i;

  fill_cube(0x00);

  for (i=0; i<8; i++) {
    set_voxel(i,0,0,1);
    set_voxel(i,0,7,1);
    set_voxel(i,7,0,1);
    set_voxel(i,7,7,1);
    set_voxel(0,i,0,1);
    set_voxel(0,i,7,1);
    set_voxel(7,i,0,1);
    set_voxel(7,i,7,1);
    set_voxel(0,0,i,1);
    set_voxel(0,7,i,1);
    set_voxel(7,0,i,1);
    set_voxel(7,7,i,1);
  }
 
}

void random_filler(int state) {
  int x,y,z;
  const double delay = 2200;
  if (state == 1) {
    fill_cube(0x00);
  } else {
    fill_cube(0xFF);
  }
  int loop = 0;
  while (loop<512) {
    x = rand_lower_than(8);
    y = rand_lower_than(8);
    z = rand_lower_than(8);
    if (state == 0 && get_voxel(x,y,z)) {
      set_voxel(x,y,z,0);
      _delay_us(delay);
      loop += 1;
    } else if (state == 1 && !get_voxel(x,y,z)) {
      set_voxel(x,y,z,1);
      _delay_us(delay);
      loop += 1;
    }
  }
}

void loadbar(void) {
  int x,y,z;
  const double delay = 40000;
  fill_cube(0x00);
  for (z=0; z<8; z++) {
    for (x=0; x<8; x++) {
      for (y=0; y<8; y++) {
        set_voxel(x,y,z,1);
      }
    }
    _delay_us(delay);
  }

  _delay_us(delay*3);

  for (z=0; z<8; z++) {
    for (x=0; x<8; x++) {
      for (y=0; y<8; y++) {
        set_voxel(x,y,z,0);
      }
    }
    _delay_us(delay);
  }
}

void rain(int iterations) {
  int i,it;
  int rnd_x, rnd_y;
  int rnd_num;

  fill_cube(0x00);

  for (it=0; it<iterations; it++) {
    rnd_num = rand_lower_than(4);

    for (i=0; i<rnd_num; i++) {
      rnd_x = rand_lower_than(8);
      rnd_y = rand_lower_than(8);
      set_voxel(rnd_x, rnd_y, 7, 1);
    }

    _delay_us(70000);
    shift(Z_AXIS);
  } 
}

static void send_voxel_z(uint8_t x, uint8_t y, uint8_t z, double delay) {
  uint8_t i, ii;

  for (i=0; i<8; i++) {
    if (z==7) {
      ii = 7-i;
      if (ii+1 <= 7) {
        set_voxel(x, y, ii+1, 0);
      }
    } else {
      ii = i;
      if (ii-1 >= 0) {
        set_voxel(x, y, ii-1, 0);
      }
    }
    set_voxel(x, y, ii, 1);
    _delay_us(delay);
  }
}

void send_voxels_rand_z(int iterations) {
  uint8_t x, y, last_x=0, last_y=0;
  int i;
  const double delay = 8000;
  const double wait = 70000;

  fill_cube(0x00);
  for (x=0; x<8; x++) {
    for (y=0; y<8; y++) {
      set_voxel(x, y, rand_lower_than(2)*7, 1);
    }
  }

  for (i=0; i<iterations; i++) {
    x = rand_lower_than(8);
    y = rand_lower_than(8);

    if (y != last_y && x != last_x) {
      if (get_voxel(x,y,0)) {
        send_voxel_z(x,y,0,delay);
      } else {
        send_voxel_z(x,y,7,delay);
      }
      _delay_us(wait);

      last_y = y;
      last_x = x;
    }
  }

}
