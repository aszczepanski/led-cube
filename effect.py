class Effect:
  def __init__(self, cube):
    self.cube = cube
    self.iterations = 0

  def run(self):
    while True:
      next(self)
      print(self.cube.to_string())
      self.cube.flush()
      time.sleep(0.1)
      self.iterations += 1

from smoke import SmokeEffect
from snake import SnakeEffect
from basic import BasicEffects

import time

class EffectRunner:
  def __init__(self, cube):
    self.cube = cube
  def run_effect(self, effect_name):
    if effect_name == "snake":
      effect = SnakeEffect(self.cube)
    elif effect_name == "smoke":
      effect = SmokeEffect(self.cube)
    elif effect_name == "rain":
      effect = BasicEffects(self.cube, "rain")
    elif effect_name == "random_filler":
      effect = BasicEffects(self.cube, "random_filler")
    elif effect_name == "blink":
      effect = BasicEffects(self.cube, "blink")
    elif effect_name == "loadbar":
      effect = BasicEffects(self.cube, "loadbar")
    else:
      raise ValueError
      
    effect.run()
