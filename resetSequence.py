import serial
import time
import random

s = serial.Serial('/dev/ttyUSB0', 115200)

def toPlotter(command):
  s.write(str(command + '\n').encode())

def resetSequence():
  toPlotter("\r\n\r")
  time.sleep(2)
  s.flushInput()

  toPlotter('$h')
  toPlotter('$1=255')
  time.sleep(1)

  toPlotter('G92x0y0')
  toPlotter('g1f1000')
  toPlotter('z5')
  time.sleep(2)

  toPlotter('z0f1000')
  time.sleep(1)

  toPlotter('$1=0')
  time.sleep(1)

  toPlotter('x10y10')
