#ifndef EFFECTS_H_
#define EFFECTS_H_

#include <stdint.h>

#define BOTTOM_TOP 0x01
#define TOP_BOTTOM 0x02
#define LEFT_RIGHT 0x04
#define RIGHT_LEFT 0x08
#define FRONT_BACK 0x10
#define BACK_FRONT 0x20


void launch_effect(int effect);

void rain(int iterations);

void send_voxels_rand_z(int iterations);

void turn_on_and_off_each_layer(unsigned char direction);
void set_edges(void);
void random_diodes(void);
void random_filler(int state);
void loadbar(void);

#endif  // EFFECTS_H_
