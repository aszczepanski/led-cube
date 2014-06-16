import ledcube
import serial

from pubsub import Subscriber

def bin(s):
  return str(s) if s<=1 else bin(s>>1) + str(s&1)

class UART(Subscriber):
  def __init__(self):
    self.__serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

  def update(self, cube):
    self.__serial.write(chr(int('AB', 16)))
    self.__serial.write(chr(int('CD', 16)))
    for y in range(0,cube.size):
      for z in range(0,cube.size):
        row = 0
        for x in range(0,cube.size):
          if (cube.at((x,y,z))):
            row |= (1<<x)
        self.__serial.write(chr(row))
        if (chr(row) == chr(int('AB', 16))):
          self.__serial.write(chr(row))
        # print bin(row).zfill(self.size)

from ledcube import LEDCube

if __name__ == "__main__":
  cube = LEDCube(8)

  cube.addSubscriber(UART())
  cube.on((7,7,7))
  cube.flush()
