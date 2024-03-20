from setup import resetSequence
from setup import resetSequence
import keyboard

# resetSequence()

def on_key_press(event):
  print(event.name)
    # print(f"You pressed {event.name}")

keyboard.add_hotkey('ctrl+alt+a', on_key_press)
keyboard.wait()

# input()


# while True:
#   try:
#     key = keyboard.read_key()
#     if key == 'up':
#       print('up')
#     elif key == 'down':
#       print('down')
#     elif key == 'left':
#       print('left')
#     elif key == 'right':
#       print('right')
#     else:
#       print('Invalid key')
#   except KeyboardInterrupt:
#     break
