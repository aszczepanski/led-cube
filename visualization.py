import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

size = 4
count = size ** 3
cm = plt.get_cmap("RdYlGn")

points = np.arange(0, count)
points = [ [point / size ** 2, point / size % size, point % size] for point in points ]

x = [ point[0] for point in points ]
y = [ point[1] for point in points ]
z = [ point[2] for point in points ]
col = np.arange(len(x))

fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
p3d = ax3D.scatter(x, y, z, s=count, c=col, marker='o')

plt.show()
