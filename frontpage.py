import webbrowser          # import webbrowser
import pyautogui as control  # import pyautogui for mouse control
import time                # import time
import schedule            # import schedule
def mainfile():

    def work():
        webbrowser.open(
            "https://online.karunya.edu/oauth/login?access=student")  # Enter the webpage that you want to open.
        # use python IDLE and type import puautogui and use mouse.position() to find x and y axix of your mouse at any location
        time.sleep(5)
        control.hotkey('tab')
        control.press('enter')
        time.sleep(3)
        control.hotkey('ctrlleft', 'w')
        time.sleep(1)
        webbrowser.open("https://online.karunya.edu/students/home")
# The main screen of our script
    print('''
                Welcome To Class Automation System
    Press (1) ---> to start and run the automation
    ''')
    user_input = 1

    if user_input == 1:
        #change the time with the time of your classes
        schedule.every().day.at("08:55").do(work)
        schedule.every().day.at("09:55").do(work)
        schedule.every().day.at("10:55").do(work)
        schedule.every().monday.at("11:55").do(work)
        schedule.every().tuesday.at("11:55").do(work)
        schedule.every().thursday.at("11:55").do(work)
        schedule.every().monday.at("13:55").do(work)
        schedule.every().tuesday.at("13:55").do(work)
        schedule.every().friday.at("13:55").do(work)
        schedule.every().monday.at("14:55").do(work)

    # its a small code so that the code keeps running on and on
    while True:
        schedule.run_pending()
        time.sleep(1)

    # LETS SHARE KNOWLEDGE _CHOTA_CODER_




