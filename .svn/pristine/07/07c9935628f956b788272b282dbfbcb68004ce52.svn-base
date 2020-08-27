import time
from pynput.mouse import Button
from pynput.keyboard import Key
from pynput.keyboard import Controller
from pynput.mouse import Controller as controller


def control_mouse():
    while True:
        mouse = controller()
        print("The current pointer position is {0}".format(mouse.position))
        time.sleep(2)
        mouse.position = (10, 20)
        print("Now we have moved it to {0}".format(mouse.position))
        time.sleep(2)
        mouse.move(5, -5)
        time.sleep(2)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(2)
        mouse.click(Button.left, 2)
        time.sleep(2)
        mouse.scroll(0, 2)
        time.sleep(2)


def control_keypad():
    while True:
        time.sleep(60)
        keyboard = Controller()
        time.sleep(2)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(2)
        keyboard.press('a')
        keyboard.release('a')
        time.sleep(2)
        keyboard.press('A')
        keyboard.release('A')
        time.sleep(2)
        with keyboard.pressed(Key.shift):
            keyboard.press('a')
            keyboard.release('a')
        time.sleep(2)
        keyboard.type('Hello World!')


if __name__ == '__main__':
    # control_mouse()
    control_keypad()

"""
import pyautogui
import time
cposition = pyautogui.locateOnScreen('c.png')  #根据图片定位
cc = pyautogui.center(cposition)  #获取这个软件位置的中心
print(cposition)
print(cc)
pyautogui.moveTo(cc[0],cc[1])  #把鼠标移动到这个位置
pyautogui.click(clicks=2)   #点击两下，实现双击

pyautogui的键盘功能：
打字功能：
这里可以实现给定一串英文字符，然后直接打出
import pyautogui
pyautogui.typewrite('Hello world!', interval=0.25)
其中interval是间隔时间，0.25就是1/4秒。
键盘操作还有press()，keyup(),keydown(),和热键hotkey()四个函数
其中press就是keyup和keydown合并起来的函数，
keyup就是按键抬起，keydown就是按键按下
import pyautogui
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left'])
pyautogui.keyUp('shift')
hotkey()就是可以让你连续的按下几个键然后按相反顺序释放。
"""

"""
os.system("pytest --html=report.html")
os.system("python ./test_clinic_scenario_part.py")
import subprocess
subprocess.Popen()
"""

"""
#coding=utf-8
#!/usr/bin/python
import os
def open_app(app_dir):
  os.startfile(app_dir)
if __name__ == "__main__":
  app_dir = r'C:\Program Files\Sublime Text 2\sublime_text.exe'
  open_app(app_dir)

扩展资料：
终止应用程序脚本    
#coding=utf-8
import os
#终止QQ软件
os.system("taskkill /F /IM QQ.exe")
#终止日报订餐软件
os.system("taskkill /F /IM Pudding.exe")
#终止OA软件
os.system("taskkill /F /IM ispiritPro.exe")
"""
