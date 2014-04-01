import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

size = 4
count = size ** 3

points = np.arange(0, count)
points = [ [point / size ** 2, point / size % size, point % size] for point in points ]

x = [ point[0] for point in points ]
y = [ point[1] for point in points ]
z = [ point[2] for point in points ]

leds = [ 1 if np.random.rand() > 0.5 else 0 for i in np.arange(0, count) ]

col = [ [0.0, 0.0, 1.0, i] for i in leds ]

fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
p3d = ax3D.scatter(x, y, z, s=count, c=col, marker='o')

plt.show()
