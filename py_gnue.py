import time

import pyautogui
from time import sleep

##
# пауза и досрочное прекращение
pyautogui.PAUSE = 1.5

pyautogui.FAILSAFE = True
##
# разрешение и позиция

# sleep(1.5)
print('-'*100)

print(pyautogui.size())

print(pyautogui.position())
# ##
# # перемещение мыши
pyautogui.moveTo(32, 65, duration=1)
# pyautogui.move(-200, -200, duration=1)
# pyautogui.move(-200, 200, duration=1)
# pyautogui.move(340, 0, duration=1)
# ##
# # нажатие
# pyautogui.click()
pyautogui.rightClick()
# pyautogui.doubleClick()
# pyautogui.tripleClick()
# pyautogui.rightClick()
# pyautogui.vscroll(-200)
# pyautogui.middleClick()
# ##
# # перемещение с зажатием
# # pyautogui.position()
# pyautogui.moveTo(491, 412, duration=1)
# pyautogui.dragTo(125, 412, duration=1)
# pyautogui.move(100, None, duration=1)
# ##
# # ввод с клавиатуры
# sleep(0.5)
# pyautogui.typewrite('Hello, World!', interval=0.2)
# ##
# # нажатие клавиш: press, hotkey
# sleep(0.5)
# pyautogui.press('enter')
# pyautogui.hotkey('ctrl', 'a')
# ##
# # скриншоты и нахождение отдельных элементов
pyautogui.screenshot(r"/home/ser4/PycharmProjects/kurs1/skrin1.png")
# pyautogui.locateCenterOnScreen(r"C:\Users\Артём Владимирович\Downloads\text.png")
# pyautogui.click()
