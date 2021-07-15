import keyboard
import os
from coord import Coord
from display import Display



os.system('cls||clear')
d = Display()
d.veisible_disp(d.disp_x())
kl = Coord()
k_up = kl.up
k_down = kl.down
s_left = kl.left
s_right = kl.right
s_enter = kl.enter_


keyboard.add_hotkey('up', k_up)
keyboard.add_hotkey('down', k_down)
keyboard.add_hotkey('right', s_right)
keyboard.add_hotkey('left', s_left)
keyboard.add_hotkey('enter', kl.enter_)
keyboard.wait('Ctrl + Q')