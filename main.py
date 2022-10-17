import pyautogui as pg
import webbrowser as wb
import time as t

wb.open("web.whatsapp.com")
t.sleep(2)

for i in range(1000):
    pg.typewrite("hi")
    pg.press("enter")
