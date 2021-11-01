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


def send_message_to_discord():
    time.sleep(1)
