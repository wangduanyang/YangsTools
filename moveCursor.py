import pyautogui
import random

pyautogui.PAUSE = 500
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
#i = 2

#step = random.randrange(-1, 1)
#print(step)
while True:
    x, y = pyautogui.position()
    step = random.randrange(-50, 50)
    print(step)
    x += step
    y += step
    try:
        pyautogui.moveTo(x, y)
    except Exception as e:
        raise
    else:
        pass
    finally:
        pass
   
	
