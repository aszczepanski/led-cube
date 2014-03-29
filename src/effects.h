#ifndef EFFECTS_H_
#define EFFECTS_H_

#define BOTTOM_TOP 0x01
#define TOP_BOTTOM 0x02
#define LEFT_RIGHT 0x04
#define RIGHT_LEFT 0x08
#define FRONT_BACK 0x10
#define BACK_FRONT 0x20


void turn_on_and_off_each_layer(unsigned char direction);
void random_diodes(void);

#endif  // EFFECTS_H_
