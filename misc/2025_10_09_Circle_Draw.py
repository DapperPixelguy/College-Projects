import os, subprocess
import math
import pyautogui

coords = subprocess.check_output("hyprctl cursorpos", shell=True, text=True)
x, y = coords.strip().split(',')
x, y = int(x), int(y)
os.environ["YDOTOOL_SOCKET"] = "/tmp/.ydotool_socket"
import time

print(coords)

def draw_circle(r):
    for degree in range(0,360):
        angle = math.radians(degree)
        new_x = x + r * math.cos(angle)
        new_y = y + r * math.sin(angle)
        os.system(f'ydotool mousemove {new_x} {new_y}')
        # pyautogui.moveTo(x + r * math.cos(angle * math.pi / 180),
        #                  y + r * math.sin(angle * math.pi / 180))
        time.sleep(0.005)

def read_pos():
    while True:
        x, y = pyautogui.position()
        print(x,y)\

#read_pos()
draw_circle(150)

