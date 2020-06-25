import webbrowser
import time
import pyautogui as gui

numbers=[919177227737,919949702217]

msg=""

c=1
for i in numbers:
    if c==1:
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(12)
        gui.keyDown('ctrl')
        gui.press('w')
        gui.keyUp('ctrl')
        time.sleep(8)
        c+=1
    url="https://web.whatsapp.com/send?phone={}&text={}&source&data&app_absent".format(i,msg)
    webbrowser.open(url)
    time.sleep(12)
    gui.keyDown('ctrl')
    gui.press('v')
    gui.keyUp('ctrl')
    time.sleep(1)
    gui.press('enter')
    time.sleep(2)
    gui.keyDown('ctrl')
    gui.press('w')
    gui.keyUp('ctrl')
    time.sleep(8)
