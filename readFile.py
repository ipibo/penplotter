import serial
import time
import random
import math

file = open("accessibility.gcode", "r")
# file = open("card.ngc", "r")
# file = open("square.ngc", "r")

s = serial.Serial('/dev/ttyUSB0', 115200)

s.write("\r\n\r\n".encode())
time.sleep(2)
s.flushInput()

s.write(str('$h\n').encode())
s.write(str('$1=255\n').encode())
time.sleep(1)
s.write(str('G92x0y0\n').encode())
s.write(str('g1f5000\n').encode())
s.write(str('z5\n').encode())
time.sleep(10)

print("start moving")

counter = 0
rowCounter = 0

for line in file:
  l = line.strip()  # Strip all EOL characters for consistency
  print('Sending: ' + l)
  s.write(l + '\n')  # Send g-code block to grbl
  grbl_out = s.readline()  # Wait for grbl response with carriage return
  print(' : ' + grbl_out.strip())

'''
for line in file:
  print('{} on row {}'.format(line, rowCounter))
  rowCounter = rowCounter + 1
  if line.startswith('G'):
    thisLine = "{}\n".format(line)
    s.write(str(thisLine).encode())

    grbl_out = s.readline()  # Wait for grbl response with carriage return
    print(' : ' + grbl_out.strip())

    if counter > 1000:
      break

    if "Penetrate" in line:
      time.sleep(0.5)
    else:
      time.sleep(0.02)

    counter = counter + 1
'''

print("closing")

time.sleep(1)
s.write(str('z0f1000\n').encode())
time.sleep(5)
s.write(str('$1=0\n').encode())
time.sleep(2)
s.write(str('x10y10\n').encode())
s.close()
