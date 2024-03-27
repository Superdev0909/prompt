import pyautogui
import time
import random
t=0
while (t < 200):
    t+=1
    # # Give yourself a few seconds delay to switch to another window or prepare for the action
    # time.sleep(10)
    # Repeat the movement 5 times
    for _ in range(3):
        # Get screen size
        screen_width, screen_height = pyautogui.size()
        # Generate random x, y coordinates
        random_x = random.randint(100, screen_width - 100)
        random_y = random.randint(100, screen_height - 100)
        # Move the mouse to the random coordinates
        pyautogui.moveTo(random_x, random_y, duration=1)
        # Randomly choose between 1 and -1

        dir = random.choice([-1, 1])
        # Randomly choose scroll amount

        amount = random.randint(500, 2000)
        # Scroll up 10 "clicks"
        pyautogui.scroll(amount * dir)
        # Wait a second before moving again
        time.sleep(5)
    # Press down the 'alt' key
    pyautogui.keyDown('alt')
    # Press the 'tab' key once
    random_int = random.randint(1, 7)
    while (random_int != 0):
        pyautogui.press('tab')
        random_int = random_int - 1
    # You might want to wait a bit between pressing 'tab' if you want to switch more applications
    time.sleep(1)
    # Release the 'alt' key
    pyautogui.keyUp('alt')