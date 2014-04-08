import numpy as np
import string

import serial

def bin(s):
  return str(s) if s<=1 else bin(s>>1) + str(s&1)

class LEDCube:
  def __init__(self, size):
    self.size = size
    self.count = size ** 3
    self.points = np.arange(0, self.count)
    self.point_numbers = np.arange(0, self.count)
    self.clear()

    self.__serial = serial.Serial('/dev/ttyUSB0', 250000, timeout=1)

  def flush(self):
    self.__serial.write(chr(int('AB', 16)))
    for y in range(0,self.size):
      for z in range(0,self.size):
        row = 0
        for x in range(0,self.size):
          if (self.points[self.__point_to_number((x,y,z))]):
            row |= (1<<x)
        self.__serial.write(chr(row))
        print bin(row).zfill(self.size)

  def randomness(self):
    self.points = [ np.random.rand() > 0.5 for i in self.points ]

  def clear(self):
    self.points.fill(False)

  def fill(self):
    self.points.fill(True)

  def on(self, point):
    self.points[self.__point_to_number(point)] = True

  def off(self, point):
    self.points[self.__point_to_number(point)] = False

  def layer(self, number, direction):
    if direction == 0:
      ary = [ i / self.size ** 2 == number for i in self.point_numbers ]
    elif direction == 1:
      ary = [ i / self.size % self.size == number for i in self.point_numbers ]
    elif direction == 2:
      ary = [ i % self.size == number for i in self.point_numbers ]
    self.__light_up(ary)

  def to_string(self):
    return string.join([ '1' if i else '0' for i in self.points ], '')

  def __light_up(self, points):
    self.points = np.array([ i[0] or i[1] for i in zip(self.points, points) ])

  def __point_to_number(self, point):
    return point[1] * (self.size ** 2) + point[2] * self.size + point[0]
