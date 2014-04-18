import numpy
import time

class BasicEffects:
  def __init__(self, cube, effect_name):
    self.cube = cube
    self.effect_name = effect_name

  def run(self):
    self.cube.clear()
    self.cube.flush()

    if self.effect_name == "rain":
      self.sendvoxels_rand_y(150, 0.015, 0.09)
    elif self.effect_name == "random_filler":
      self.random_filler(0.02, 1)
      self.random_filler(0.02, 0)
    elif self.effect_name == "blink":
      self.blink(4)
    elif self.effect_name == "loadbar":
      self.loadbar(0.1)
      self.loadbar(0.1)

    elif self.effect_name == "demo":
      self.cube.clear()
      self.cube.flush()

      self.loadbar(0.1)
      self.loadbar(0.1)

      self.sendvoxels_rand_y(100, 0.015, 0.09)

      self.random_filler(0.02, 1)
      self.random_filler(0.02, 0)

      self.blink(2)
      
    else:
      raise ValueError


  def __sendvoxel_y(self, (x, y, z), delay):
    for i in range(4):
      if y==3:
        ii = 3-i
        if ii+1 <= 3:
          self.cube.off((x,ii+1,z))
      else:
        ii = i
        if ii-1 >= 0:
          self.cube.off((x,ii-1,z))
      self.cube.on((x,ii,z))
      self.cube.flush()
      time.sleep(delay)

  def sendvoxels_rand_y(self, iterations, delay, wait):
    loop = 16;

    self.cube.clear();

    last_x = last_z = -1

    for x in range(4):
      for z in range(4):
        if (numpy.random.randint(0,2) == 0):
          self.cube.on((x,0,z))
        else:
          self.cube.on((x,3,z))

    self.cube.flush()

    for i in range(iterations):
      x = numpy.random.randint(0,4)
      z = numpy.random.randint(0,4)

      if (x != last_x and z != last_z):
        if self.cube.at((x,0,z)):
          self.__sendvoxel_y((x,0,z),delay)
        else:
          self.__sendvoxel_y((x,3,z),delay)
        time.sleep(wait)
        last_x = x
        last_z = z

  def random_filler(self, delay, state):
    if state == 1:
      self.cube.clear()
    else:
      self.cube.fill()
    loop = 0;
    while (loop<63):
      x = numpy.random.randint(0,4)
      y = numpy.random.randint(0,4)
      z = numpy.random.randint(0,4)
      if state == 0 and self.cube.at((x,y,z)):
        self.cube.off((x,y,z))
        self.cube.flush()
        time.sleep(delay)
        loop += 1
      elif state == 1 and self.cube.at((x,y,z))==False:
        self.cube.on((x,y,z))
        self.cube.flush()
        time.sleep(delay)
        loop += 1

  def loadbar(self, delay):
    self.cube.clear();
    for y in range(4):
      for x in range(4):
        for z in range(4):
          self.cube.on((x,y,z))
      self.cube.flush()
      time.sleep(delay)

    time.sleep(delay*3)

    for y in range(4):
      for x in range(4):
        for z in range(4):
          self.cube.off((x,y,z))
      self.cube.flush()
      time.sleep(delay);

  def blink(self, iterations):
    self.cube.clear()
    self.cube.flush()
    time.sleep(2)

    for a in range(iterations):
      self.cube.fill();
      self.cube.flush()
      time.sleep(0.05)
      self.cube.clear()
      self.cube.flush()
      time.sleep(1.5)
      self.cube.fill()
      self.cube.flush()
      time.sleep(0.03)
      self.cube.clear()
      self.cube.flush()
      time.sleep(2)

