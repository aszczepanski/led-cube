#!/usr/bin/env python

import numpy as np
import scikits.audiolab as audiolab
import pyaudio
from threading import Thread
import time, wave, sys

sound = audiolab.Sndfile('sound.wav')
samplerate = sound.samplerate
data = sound.read_frames(samplerate * 120)
data_mono = data[:,0]
data_stereo = data.transpose()

def transform_window(window):
  return np.max(np.absolute(window))

def print_window(window, cube_size):
  ones = int(cube_size * window)
  zeroes = cube_size - ones
  prints = [ "1" for i in range(ones) ]
  for i in range(zeroes):
    prints.append("0")
  sys.stdout.write("\r" +  "".join(prints))
  sys.stdout.flush()

def print_windows(windows, cube_size, window_size, samplerate):
  interval = float(window_size) / samplerate
  for window in windows:
    time.sleep(interval)
    print_window(window, cube_size)

def play_data(data, samplerate):
  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paFloat32, channels=2, rate=samplerate, output=True)
  stream.write(data.astype(np.float32).tostring())
  stream.close()
  p.terminate()

window_size = samplerate / 16
windows_count = len(data) / window_size
windows = [ transform_window(data_mono[i*window_size:(i+1)*window_size]) for i in range(0, windows_count) ]

cube_size = 4 ** 3

thread1 = Thread(target = play_data, args=(data, samplerate))
thread2 = Thread(target = print_windows, args=(windows, cube_size, window_size, samplerate))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("STOP")
