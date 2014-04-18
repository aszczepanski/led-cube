#!/usr/bin/env python -u

from ledcube import LEDCube

from effect import EffectRunner

import sys
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

if args.output:
  if 'serial' in args.output:
    cube.addSubscriber(communication.UART())
  if 'matplotlib' in args.output:
    cube.addSubscriber(visualization.MatplotlibVisualizator())
  if 'opengl' in args.output:
    cube.addSubscriber(visualization.OpenGLVisualizator())
  
effectRunner = EffectRunner(cube)
if args.effect == "demo":
  effectRunner.run_demo()
else:
  effectRunner.run_effect(args.effect)
