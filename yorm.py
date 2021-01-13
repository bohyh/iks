import cv2 as cv
import numpy as np
import os
import pyautogui

if __name__ == '__main__':
    def nothing(*arg):
        pass

cv.namedWindow("result")  # создаем главное окно
cv.namedWindow("settings")  # создаем окно настроек

cv.createTrackbar('h1', 'settings', 0, 255, nothing)
cv.createTrackbar('s1', 'settings', 0, 255, nothing)
cv.createTrackbar('v1', 'settings', 0, 255, nothing)
cv.createTrackbar('h2', 'settings', 255, 255, nothing)
cv.createTrackbar('s2', 'settings', 255, 255, nothing)
cv.createTrackbar('v2', 'settings', 255, 255, nothing)
crange = [0, 0, 0, 0, 0, 0]

while(True):

    # get an updated image of the game
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    # screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    hsv = cv.cvtColor(screenshot, cv.COLOR_RGB2HSV)
    # считываем значения бегунков
    h1 = cv.getTrackbarPos('h1', 'settings')
    s1 = cv.getTrackbarPos('s1', 'settings')
    v1 = cv.getTrackbarPos('v1', 'settings')
    h2 = cv.getTrackbarPos('h2', 'settings')
    s2 = cv.getTrackbarPos('s2', 'settings')
    v2 = cv.getTrackbarPos('v2', 'settings')
    # формируем начальный и конечный цвет фильтра
    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)
    # накладываем фильтр на кадр в модели HSV
    thresh = cv.inRange(hsv, h_min, h_max)

    cv.imshow('result', thresh)
    # cv.imshow('Computer Vision', screenshot)



    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
