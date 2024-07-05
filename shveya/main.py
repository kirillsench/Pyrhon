import pyautogui
import numpy as np
import cv2
import time
import keyboard


def get_scaled_region(base_res, current_res, base_region):
    scale_x = current_res[0] / base_res[0]
    scale_y = current_res[1] / base_res[1]
    scaled_region = (
        int(base_region[0] * scale_x),
        int(base_region[1] * scale_y),
        int(base_region[2] * scale_x),
        int(base_region[3] * scale_y)
    )
    return scaled_region


def show_region(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot_np = np.array(screenshot)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    cv2.rectangle(screenshot_np, (0, 0), (region[2], region[3]), (0, 255, 0), 2)
    cv2.imshow('Region', screenshot_np)
    cv2.waitKey(1)  # Показать изображение на 1 секунду


base_resolution = (2560, 1600)  # Базовое разрешение
current_resolution = pyautogui.size()  # Текущее разрешение экрана
base_region = (1220, 790, 120, 80)  # Базовые координаты и размеры региона

scaled_region = get_scaled_region(base_resolution, current_resolution, base_region)
show_region(scaled_region)

wW = cv2.imread("./working_W.png")
wA = cv2.imread("./working_A.png")
wS = cv2.imread("./working_S.png")
wD = cv2.imread("./working_D.png")

time.sleep(2)

while True:
    if keyboard.is_pressed('esc'):
        break

    shot = np.array(pyautogui.screenshot(region=scaled_region))
    shot_gray = cv2.cvtColor(shot, cv2.COLOR_BGR2GRAY)

    wW_gray = cv2.cvtColor(wW, cv2.COLOR_BGR2GRAY)
    wA_gray = cv2.cvtColor(wA, cv2.COLOR_BGR2GRAY)
    wS_gray = cv2.cvtColor(wS, cv2.COLOR_BGR2GRAY)
    wD_gray = cv2.cvtColor(wD, cv2.COLOR_BGR2GRAY)

    matchW = cv2.matchTemplate(shot_gray, wW_gray, cv2.TM_CCOEFF_NORMED)
    matchA = cv2.matchTemplate(shot_gray, wA_gray, cv2.TM_CCOEFF_NORMED)
    matchS = cv2.matchTemplate(shot_gray, wS_gray, cv2.TM_CCOEFF_NORMED)
    matchD = cv2.matchTemplate(shot_gray, wD_gray, cv2.TM_CCOEFF_NORMED)

    threshold = 0.6
    if np.max(matchW) >= threshold:
        pyautogui.press('w')
    elif np.max(matchA) >= threshold:
        pyautogui.press('a')
    elif np.max(matchS) >= threshold:
        pyautogui.press('s')
    elif np.max(matchD) >= threshold:
        pyautogui.press('d')
    else:
        pyautogui.press('e')

    time.sleep(0.3)

    # Показать текущий скриншот с областью поиска
    cv2.imshow('Shot', shot_gray)

    # Закрыть окно по нажатию 'esc'
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()