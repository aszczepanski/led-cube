import numpy as np
import scikits.audiolab as audiolab
import pyaudio
from threading import Thread
import time, wave, sys

class SoundEffect:
  def __init__(self, cube, filename):
    self.cube = cube
    self.filename = filename

  def run(self):
    self.cube.clear()
    self.cube.flush()

    sound = audiolab.Sndfile('sound.wav')
    samplerate = sound.samplerate
    data = sound.read_frames(samplerate * 120)
    data_mono = data[:,0]
    data_stereo = data.transpose()

    window_size = samplerate / 16
    windows_count = len(data) / window_size
    windows = [ self.transform_window(data_mono[i*window_size:(i+1)*window_size]) for i in range(0, windows_count) ]

    thread1 = Thread(target = self.play_data, args=(data, samplerate))
    thread2 = Thread(target = self.print_windows, args=(windows, window_size, samplerate))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

  def transform_window(self, window):
    return np.max(np.absolute(window))

  def print_window(self, window):
    ones = int(self.cube.count * window)
    zeroes = self.cube.count - ones
    for i in range(ones):
      self.cube.on((i % self.cube.size, (i / self.cube.size ** 2) % self.cube.size , (i / self.cube.size) % self.cube.size))
    for i in range(ones, zeroes + ones):
      self.cube.off((i % self.cube.size, (i / self.cube.size ** 2) % self.cube.size , (i / self.cube.size) % self.cube.size))
    #print("".join(prints))
    #self.cube.randomness()

  def print_windows(self, windows, window_size, samplerate):
    interval = float(window_size) / samplerate
    for window in windows:
      time.sleep(interval)
      self.print_window(window)
      self.cube.flush()

  def play_data(self, data, samplerate):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=2, rate=samplerate, output=True)
    stream.write(data.astype(np.float32).tostring())
    stream.close()
    p.terminate()

