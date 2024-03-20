from setup import resetSequence
from setup import toPlotter
# resetSequence()

def on_key_press(event):
  print(event.name)
    # print(f"You pressed {event.name}")



def print_user_input():
  xCoord = input("enter a x coordinate:")
  print(xCoord)
  yCoord = input("enter a y coordinate:")
  print(yCoord)
  speed = input("enter a speed:")
  print(speed)
  coord = "x{0}y{1}f{2}\n".format(xCoord, yCoord, speed)
  coord = str(coord)
  toPlotter(coord)
  print(coord)
  
  



print_user_input()

