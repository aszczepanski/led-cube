#!/usr/bin/env python -u

from ledcube import LEDCube

import time, sys, string
import numpy as np

cube = LEDCube(4)
frames = 0

def frame():
  time.sleep(0.05)

def print_cube(cube):
  output = [ '1' if i else '0' for i in cube.points ]
  print(string.join(output, ''))

while True:
  if frames < 3 * cube.size:
    cube.layer(frames % cube.size, frames / cube.size)
  else:
    cube.randomness()

  print_cube(cube)

  frames += 1
  frame()
