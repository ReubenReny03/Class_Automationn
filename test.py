import time
import webbrowser
import pyautogui as control

def work():
    webbrowser.open("https://online.karunya.edu/oauth/login?access=student") #Enter the webpage that you want to open.
# use python IDLE and type import puautogui and use mouse.position() to find x and y axix of your mouse at any location
    time.sleep(5)
    control.hotkey('tab')
    control.press('enter')
    time.sleep(3)
    control.hotkey('ctrlleft','w')
    time.sleep(1)
    webbrowser.open("https://online.karunya.edu/students/home")