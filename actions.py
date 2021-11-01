import pyautogui as pg
import time


def open_game():
    time.sleep(0.5)
    pg.hotkey('alt', 'tab')
    time.sleep(0.5)


def make_search(name):
    pg.dragTo(210, 240)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    pg.typewrite(name, interval=0.1)