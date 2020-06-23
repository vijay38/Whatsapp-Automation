import webbrowser
import time
import pyautogui as gui

numbers=["+919177227737"]

msg="Hey this is sent through python script!its awesome!!"

for i in numbers:
    url="https://web.whatsapp.com/send?phone={}&text={}&source&data&app_absent".format(i,msg)
    webbrowser.open(url)
    time.sleep(12)
    gui.press('enter')
    time.sleep(2)
    gui.keyDown('ctrl')
    gui.press('w')
    gui.keyUp('ctrl')
    time.sleep(8)
