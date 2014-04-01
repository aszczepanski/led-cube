#!/usr/bin/env python -u

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

size = 4
count = size ** 3

points = np.arange(0, count)
points = [ [point / size ** 2, point / size % size, point % size] for point in points ]

x = [ point[0] for point in points ]
y = [ point[1] for point in points ]
z = [ point[2] for point in points ]

fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')

plt.ion()
plt.show()

for line in sys.stdin:
  print("Received line: " + line.strip())
  leds = [ int(i) for i in line.strip() ]
  col = [ [0.0, 0.0, 1.0, i] for i in leds ]
  ax3D.clear()
  p3d = ax3D.scatter(z, y, x, s=count, c=col, marker='o')
  plt.draw()
