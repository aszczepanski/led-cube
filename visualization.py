#!/usr/bin/env python -u

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

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

class OpenGLVisualizator(Subscriber):
  def __init__(self):
    self.name = 'LED cube'

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600,600)
    glutCreateWindow(self.name)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glEnable( GL_BLEND );

    glClearColor(0.,0.,0.,1.)
    #glShadeModel(GL_SMOOTH)
    #glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    #lightZeroPosition = [10.,4.,10.,1.]
    #lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    #glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    #glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    #glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    #glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    #glutDisplayFunc(self.display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(65.,1.,1.,65.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(11,12,15,
      0,0,0,
      0,1,0)
    glPushMatrix()
    #glutMainLoop()

  def update(self, cube):
    self.display(cube)

  def display(self,cube):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    for x in range(4):
      for y in range(4):
        for z in range(4):
          glPushMatrix()

          glTranslate(-4.5+3*x,-4.5+3*y,4.5-3*z)

          glDisable(GL_LIGHTING)

          glColor4f(0.1,0.1,0.1, 0.8)
          glLineWidth(0.1)

          if (z > 0):
            glBegin(GL_LINES)
            glVertex3f(0,0,0)
            glVertex3f(0,0,3)
            glEnd()
          if (y < 3):
            glBegin(GL_LINES)
            glVertex3f(0,0,0)
            glVertex3f(0,3,0)
            glEnd()
          if (x < 3):
            glBegin(GL_LINES)
            glVertex3f(0,0,0)
            glVertex3f(3,0,0)
            glEnd()

          glEnable(GL_LIGHTING)

          if (cube.at((x,y,z))):
            color = [0.15, 1.0, 0.15, 0.95]
          else:
            color = [0.0, 0.15, 0.0, 0.55]
          glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
          glutSolidSphere(0.26,20,20)

          glPopMatrix()
    glutSwapBuffers()

