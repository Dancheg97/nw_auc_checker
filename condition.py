import pyautogui as pg
from PIL import Image
import numpy as np
import cv2

wait_image = Image.open('wait.png')
pull_image = Image.open('pull.png')
pull2_image = Image.open('pull2.png')


def get_conditions():
    img = pg.screenshot(region=(750, 150, 1200, 800))
    res_wait = cv2.matchTemplate(
        np.asarray(img),
        np.asarray(wait_image),
        cv2.TM_CCOEFF_NORMED,
    )
    threshold = .8
    loc = np.where(res_wait >= threshold)
    wait_found = len(loc[0]) != 0
    res_pull = cv2.matchTemplate(
        np.asarray(img),
        np.asarray(pull_image),
        cv2.TM_CCOEFF_NORMED,
    )
    threshold = .8
    loc = np.where(res_pull >= threshold)
    pull_found = len(loc[0]) != 0
    res_pull = cv2.matchTemplate(
        np.asarray(img),
        np.asarray(pull2_image),
        cv2.TM_CCOEFF_NORMED,
    )
    threshold = .8
    loc = np.where(res_pull >= threshold)
    pull_found2 = len(loc[0]) != 0
    return wait_found, pull_found, pull_found2
