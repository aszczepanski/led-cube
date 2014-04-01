#!/usr/bin/env python -u

import time, sys

def frame():
  time.sleep(0.05)

size = 4
count = size ** 3
i = 0

while True:
  print('0' * i + '1' + '0' * (count - i - 1))
  i += 1
  i %= count
  frame()
