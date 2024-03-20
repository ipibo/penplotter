from setup import resetSequence
from setup import toPlotter
import os


resetSequence()


def on_key_press(event):
  print(event.name)
    # print(f"You pressed {event.name}")

def setSpeed(speed):
  toPlotter("f{0}".format(speed))

def print_user_input():
  try:
    while True:
      xCoord = input("enter a x coordinate:")
      print(xCoord)
      yCoord = input("enter a y coordinate:")
      print(yCoord)
      
      coord = "x{0}y{1}f{2}\n".format(xCoord, yCoord, speed)
      coord = str(coord)
      toPlotter(coord)

  except:
    print("error")
    xCoord = 10
    yCoord = 10
    speed = 1000
    coord = "x{0}y{1}f{2}\n".format(xCoord, yCoord, speed)
    coord = str(coord)
    toPlotter(coord)


  
# ask user for speed
speed = input("enter a speed:")
setSpeed(speed)



print_user_input()


