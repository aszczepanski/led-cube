#!/usr/bin/env python -u

from ledcube import LEDCube
from smoke import SmokeEffect
from snake import SnakeEffect

import time, sys
import numpy as np

if len(sys.argv) > 1:
  effect_name = sys.argv[1]
else:
  effect_name = "smoke"

cube = LEDCube(4)

if effect_name == "snake":
  effect = SnakeEffect(cube)
else:
  effect = SmokeEffect(cube)

while True:
  effect.next()
  print(cube.to_string())
  cube.flush()
  time.sleep(0.1)
