import pyautogui
import keyboard

# Set the delay between clicks to 0.01 seconds
pyautogui.PAUSE = 0.000001

def q():
    we = 1000000
    for i in range(we):

        if keyboard.is_pressed('s'):
            print("stopping")
            break
        pyautogui.doubleClick()


test = pyautogui.confirm(text="ready?", title="ready?",
                         buttons=['ready?', 'NOTREADY'])

if test == 'NOTREADY':
    quit()
else:
    q()
