# from setup import resetSequence
from setup import toPlotter
# resetSequence()
toPlotter('$h')

def on_key_press(event):
  print(event.name)
    # print(f"You pressed {event.name}")

def setSpeed(speed):
  toPlotter("f{0}".format(speed))

def print_user_input():
  while True:
    xCoord = input("enter a x coordinate:")
    print(xCoord)
    yCoord = input("enter a y coordinate:")
    print(yCoord)
    # speed = input("enter a speed:")
    # print(speed)
    coord = "x{0}y{1}f{2}\n".format(xCoord, yCoord, speed)
    coord = str(coord)
    toPlotter(coord)
    print(coord)
  


# ask user for speed
speed = input("enter a speed:")

setSpeed(speed)


print_user_input()


