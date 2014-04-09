#!/usr/bin/env python -u

from ledcube import LEDCube
from smoke import SmokeEffect
from snake import SnakeEffect

import time, sys
import numpy as np
import argparse

import communication
import visualization

parser = argparse.ArgumentParser()
parser.add_argument('--effect', required=True, metavar='EFFECT', help='execute given effect - one of the following: \'snake\' or \'smoke\'')
parser.add_argument('--output', nargs='+', metavar='OUT', help='add given output method - one or more of the following: \'serial\', \'matplotlib\' or \'opengl\'')
args = parser.parse_args()

print vars(args)

cube = LEDCube(4)

if args.effect == "snake":
  effect = SnakeEffect(cube)
elif args.effect == "smoke":
  effect = SmokeEffect(cube)
else:
  raise ValueError

if args.output:
  if 'serial' in args.output:
    cube.addSubscriber(communication.UART())
  if 'matplotlib' in args.output:
    cube.addSubscriber(visualization.MatplotlibVisualizator())
  if 'opengl' in args.output:
    cube.addSubscriber(visualization.OpenGLVisualizator())
  
while True:
  effect.next()
  print(cube.to_string())
  cube.flush()
  time.sleep(0.1)
