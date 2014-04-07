#!/usr/bin/env python

import serial
import time
import numpy as np

class Cube(object):
  def __init__(self):
    object.__init__(self)
    self.__serial = serial.Serial('/dev/ttyUSB0', 250000, timeout=1)
    self.__data = [[0]*4 for i in range(0,4)]

  def commit(self):
    self.__serial.write(chr(int('AB', 16)))
    for i in range(0,4):
      for j in range(0,4):
        self.__serial.write(chr(self.__data[i][j]))

  def clear(self):
    self.__data = [[0]*4 for i in range(0,4)]

  def fill(self):
    self.__data = [[15]*4 for i in range(0,4)]

  def set_voxel(self, (x, y, z)):
    self.__data[y][z] |= (1<<x)

  def clr_voxel(self, (x, y, z)):
    self.__data[y][z] &= ~(1<<x)

if __name__ == "__main__":
  cube = Cube()

  cube.commit()
  time.sleep(1)

  cube.clear()
  cube.commit()
  time.sleep(1)

  for x in range(0,4):
    cube.clear()
    for y in range(0,4):
      for z in range(0,4):
        cube.set_voxel((x,y,z))
    cube.commit()
    time.sleep(0.25)

  cube.fill()
  cube.commit()
  time.sleep(1)

  cube.clr_voxel((1,1,1))
  cube.clr_voxel((1,2,3))
  cube.commit()
  time.sleep(1)

  cube.set_voxel((1,1,1))
  cube.set_voxel((1,2,3))
  cube.commit()

