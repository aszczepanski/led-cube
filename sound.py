import numpy as np
import scikits.audiolab as audiolab
import scipy.signal
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
    data = sound.read_frames(sound.nframes)
    data_mono = data[:,0]
    data_stereo = data.transpose()

    window_size = samplerate / 32
    windows_count = len(data) / window_size
    windows = [ self.transform_window(data_mono[i*window_size:(i+1)*window_size]) for i in range(0, windows_count) ]

    thread1 = Thread(target = self.play_data, args=(data, samplerate))
    thread2 = Thread(target = self.print_windows, args=(windows, window_size, samplerate))

    self.start_time = time.time()
    self.data = data_mono

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

  def transform_window(self, window):
    return abs(scipy.signal.resample(np.fft.rfft(window), self.cube.size))
    #return np.max(np.absolute(np.fft.ifft(np.fft.fft(window)[300:])))

  def print_window(self, window):
    self.print_window_spectrum(window)

  def print_window_spectrum(self, window):
    maximum = 1
    for idx, value in enumerate(window):
      cutoff = float(value) / maximum * self.cube.size
      for i in range(self.cube.size):
        for l in range(self.cube.size):
          point = (l, i, idx % self.cube.size)
          if i <= cutoff:
            self.cube.on(point)
          else:
            self.cube.off(point)

  def print_window_layers(self, window):
    for idx in range(self.cube.size ** 2):
      cutoff = self.cube.size * window
      for i in range(self.cube.size):
        point = (idx % self.cube.size, i, (idx / self.cube.size) % self.cube.size)
        if i <= cutoff:
          self.cube.on(point)
        else:
          self.cube.off(point)

  def print_windows(self, windows, window_size, samplerate):
    interval = float(window_size) / samplerate
    for window in windows:
      time.sleep(interval)
      offset = int((time.time() - self.start_time) * samplerate)
      new_window = self.transform_window(self.data[(offset - window_size):offset])
      self.print_window(new_window)
      self.cube.flush()

  def play_data(self, data, samplerate):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=2, rate=samplerate, output=True)
    stream.write(data.astype(np.float32).tostring())
    stream.close()
    p.terminate()

