#!/usr/bin/env python -u

import time, sys, string
import numpy as np

size = 4
count = size ** 3
i = 0
frames = 0
points = np.arange(0, count)

def frame():
  time.sleep(0.05)

def randomness():
  random = [ '1' if np.random.rand() > 0.5 else '0' for i in np.arange(0, count) ]
  return string.join(random, '')

def layer(number, direction):
  if direction == 0:
    ary = [ '1' if i / size ** 2 == number else '0' for i in points ]
  elif direction == 1:
    ary = [ '1' if i / size % size == number else '0' for i in points ]
  elif direction == 2:
    ary = [ '1' if i % size == number else '0' for i in points ]
  return string.join(ary, '')

while True:
  if frames < 3 * size:
    print(layer(frames % size, frames / size))
  else:
    print(randomness())
  frames += 1
  frame()
