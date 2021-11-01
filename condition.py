import pyautogui as pg
from PIL import Image
import numpy as np
import cv2

wait_image = Image.open('wait.png')


def get_conditions():
    img = pg.screenshot()  # region=(750, 150, 1200, 800)
    res_wait = cv2.matchTemplate(
        np.asarray(img),
        np.asarray(wait_image),
        cv2.TM_CCOEFF_NORMED,
    )
    threshold = .8
    loc = np.where(res_wait >= threshold)
    return len(loc[0]) != 0
