import pyautogui
from time import sleep
import random

# Seconds
UP_INTERVAL = 0.1
DOWN_INTERVAL = 2

# Find the coordinates of sustain pedal button
sustain_pedal_coordinates = None
while sustain_pedal_coordinates == None:
    sustain_pedal_coordinates = pyautogui.locateCenterOnScreen("sustain_pedal_down.jpg", confidence=0.9)
    print(sustain_pedal_coordinates)

# Automate sustain pedal
while True:
    random_seconds = random.random()
    pyautogui.click(sustain_pedal_coordinates)
    sleep(UP_INTERVAL)
    pyautogui.click(sustain_pedal_coordinates)

    print(random_seconds)
    sleep(DOWN_INTERVAL + random_seconds)
