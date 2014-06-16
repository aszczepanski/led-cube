import numpy as np
import string
import time

from pubsub import Publisher

class LEDCube(Publisher):
  def __init__(self, size):
    Publisher.__init__(self)
    self.size = size
    self.count = size ** 3
    self.points = np.arange(0, self.count)
    self.point_numbers = np.arange(0, self.count)
    self.clear()

  def flush(self):
    self.notify()

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

  def at(self, point):
    return self.points[self.__point_to_number(point)]

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

if __name__ == "__main__":
  """Performs simple cube test"""
  cube_size = 8
  cube = LEDCube(cube_size)

  cube.flush()
  time.sleep(1)

  cube.fill()
  cube.flush()
  time.sleep(1)

  for x in range(0,cube_size):
    cube.clear()
    for y in range(0,cube_size):
      for z in range(0,cube_size):
        cube.on((x,y,z))
    cube.flush()
    time.sleep(0.25)

  cube.fill()
  cube.flush()
  time.sleep(1)

  cube.off((1,1,1))
  cube.off((1,2,3))
  cube.flush()
  time.sleep(1)

  cube.on((1,1,1))
  cube.on((1,2,3))
  cube.flush()

