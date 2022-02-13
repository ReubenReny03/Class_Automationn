import time
import webbrowser
import pyautogui as mouse

def work():
    webbrowser.open("https://online.karunya.edu/oauth/login?access=student") #Enter the webpage that you want to open.
# use python IDLE and type import puautogui and use mouse.position() to find x and y axix of your mouse at any location
    time.sleep(5)
    mouse.moveTo(964,592)
    time.sleep(1)
    mouse.click(964,592)
    time.sleep(2)
    mouse.moveTo(145, 658)
    time.sleep(1)
    mouse.click(145, 658)