extern volatile char tab[4][4];

void fill_layer(unsigned char layer, unsigned char value) {
  int i;
  if (layer < 4) {
    for (i=0; i<4; i++) {
      tab[layer][i] = value;
    }
  }
}

void fill_cube(unsigned char value) {
  int i;
  for (i=0; i<4; i++) {
    fill_layer(i, value);
  }
}
