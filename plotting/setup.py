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
  toPlotter('G21')
  time.sleep(1)
  

  toPlotter('x5y5')





# resetSequence()

# while counter < 10:
#   #while True:
#   randomX = random.random() * 50
#   randomY = random.random() * 200
#   randomSpeed = (random.random() * 1000) + 100
#   coord = "x{0}y{1}f5000\n".format(randomX, randomY)
#   coord = str(coord)
#   s.write(coord.encode())
#   time.sleep(3)

#   counter = counter + 1
#   print(counter)



# s.close()