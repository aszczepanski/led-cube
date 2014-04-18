from effect import Effect

class SmokeEffect(Effect):
  def next(self):
    if self.iterations < 3 * self.cube.size:
      self.cube.clear()
      self.cube.layer(self.iterations % self.cube.size, self.iterations / self.cube.size)
    else:
      self.cube.randomness()
