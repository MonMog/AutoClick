import pyautogui
import keyboard

test = pyautogui.prompt(text="ready?", title="ready?")

# Set the delay between clicks to 0.01 seconds
pyautogui.PAUSE = 0.0001

def q():
    we = 1000000
    for i in range(we):

        if keyboard.is_pressed('s'):
            print("stopping")
            break
        pyautogui.doubleClick()


q()
