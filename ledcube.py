import numpy as np
import string

class LEDCube:
  def __init__(self, size):
    self.size = size
    self.count = size ** 3
    self.points = np.arange(0, self.count)
    self.point_numbers = np.arange(0, self.count)
    self.clear()

  def randomness(self):
    self.points = [ np.random.rand() > 0.5 for i in self.points ]

  def clear(self):
    self.points.fill(False)

  def fill(self):
    self.points.fill(True)

  def layer(self, number, direction):
    if direction == 0:
      ary = [ i / self.size ** 2 == number for i in self.point_numbers ]
    elif direction == 1:
      ary = [ i / self.size % self.size == number for i in self.point_numbers ]
    elif direction == 2:
      ary = [ i % self.size == number for i in self.point_numbers ]
    self.light_up(ary)

  def light_up(self, points):
    self.points = np.array([ i[0] or i[1] for i in zip(self.points, points) ])

  def to_string(self):
    return string.join([ '1' if i else '0' for i in self.points ], '')
