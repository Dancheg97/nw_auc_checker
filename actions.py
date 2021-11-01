import pyautogui as pg
import time
from condition import get_conditions


def open_game():
    time.sleep(0.5)
    pg.hotkey('alt', 'tab')
    time.sleep(0.5)


def make_search(name) -> bool:
    time.sleep(1)
    pg.dragTo(210, 240)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    pg.typewrite(name, interval=0.1)
    time.sleep(1)
    pg.dragTo(210, 370)
    time.sleep(1)
    pg.click()
    time.sleep(2)
    rez = get_conditions()
    print(f'{name}: {rez}')
    return rez


first = True


def send_message_to_discord(name):
    global first
    time.sleep(1)
    pg.keyDown('alt')
    time.sleep(0.2)
    pg.press('tab')
    if first:
        time.sleep(0.2)
        pg.press('tab')
        first = False
    time.sleep(0.2)
    pg.keyUp('alt')
    pg.typewrite(f'FOUND: {name}', interval=0.1)
    pg.press('enter')
    time.sleep(1)
    pg.keyDown('alt')
    time.sleep(0.2)
    pg.press('tab')
    time.sleep(0.2)
    pg.keyUp('alt')
    time.sleep(0.2)
