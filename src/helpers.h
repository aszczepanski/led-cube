#ifndef HELPERS_H_
#define HELPERS_H_

#include <stdint.h>

#define X_AXIS  0x01
#define Y_AXIS  0x02
#define Z_AXIS  0x04

void fill_layer(uint8_t layer, uint8_t value);
void fill_column(uint8_t x, uint8_t y);
void fill_cube(uint8_t value);

void set_voxel(uint8_t x, uint8_t y, uint8_t z, uint8_t value);
int get_voxel(uint8_t x, uint8_t y, uint8_t z);

void shift(uint8_t axis);

#endif  // HELPERS_H_
