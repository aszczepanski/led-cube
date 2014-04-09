#!/usr/bin/env python -u

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

from pubsub import Subscriber

class MatplotlibVisualizator(Subscriber):
  def __init__(self):
    size = 4
    self.count = size ** 3

    points = np.arange(0, self.count)
    points = [ [point / size ** 2, point / size % size, point % size] for point in points ]

    self.x = [ point[0] for point in points ]
    self.y = [ point[1] for point in points ]
    self.z = [ point[2] for point in points ]

    self.fig = plt.figure()
    self.ax3D = self.fig.add_subplot(111, projection='3d')

    plt.ion()
    plt.show()

  def update(self, cube):
    line = cube.to_string()
    print("Received line: " + line.strip())
    leds = [ int(i) for i in line.strip() ]
    col = [ [0.0, 0.0, 1.0, i] for i in leds ]
    self.ax3D.clear()
    p3d = self.ax3D.scatter(self.z, self.y, self.x, s=self.count, c=col, marker='o')
    plt.draw()

