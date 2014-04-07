from effect import Effect

import numpy as np

class SnakeEffect(Effect):
  def __init__(self, cube):
    Effect.__init__(self, cube)
    self.snake = [ (0, 0, i) for i in np.arange(0, cube.size) ]

  def next(self):
    if self.iterations == 0:
      self.cube.clear()
      for point in self.snake:
        self.cube.on(point)

    around = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    head = self.snake[0]
    around_head = [ (head[0] + i[0], head[1] + i[1], head[2] + i[2]) for i in around ]
    around_head = filter(lambda i: 0 <= i[0] < self.cube.size and 0 <= i[1] < self.cube.size and 0 <= i[2] < self.cube.size, around_head)
    around_head = filter(lambda i: i not in self.snake, around_head)

    if len(around_head) > 0:
      chosen = np.random.choice(np.arange(0, len(around_head)))
      new_head = around_head[chosen]
      self.cube.off(self.snake[-1])
      self.snake = [new_head] + self.snake[:-1]
      self.cube.on(self.snake[0])

      Effect.next(self)
    else:
      self.iterations = 0
