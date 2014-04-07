#!/usr/bin/env python -u

from ledcube import LEDCube
from smoke import SmokeEffect

import time, sys
import numpy as np

cube = LEDCube(4)
effect = SmokeEffect(cube)

while True:
  effect.next()
  print(cube.to_string())
  time.sleep(0.05)
