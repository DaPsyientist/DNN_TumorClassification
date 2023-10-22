import pyautogui
import time

for i in range(768):
    time.sleep(3)  # wait for 3 seconds
    current_x, current_y = pyautogui.position()  # get current mouse position
    pyautogui.click(x=current_x, y=current_y)  # simulate mouse click at current position
