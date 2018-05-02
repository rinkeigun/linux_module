from pynput.keyboard import Key, Listener
#defining function to print when key is pressed
def on_press(key):
  print('{0} pressed'.format(
    key))
#defining function to print when key is released
def on_release(key):
  print('{0} release'.format(
    key))
  if key == Key.esc:
    # Stop listenerwsssdfgf
    return False

# Collect events until released
with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
