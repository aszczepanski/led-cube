class Effect:
  def __init__(self, cube):
    self.cube = cube
    self.iterations = 0

  def next(self):
    self.iterations += 1
