import pyautogui as pt
from time import sleep
import paperclip as pc


with open(r'C:\Users\root\Documents\code\dev\momom.txt','r') as f:
    output = f.read()

class WhatsApp:
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
    
    # Navigate to green dot
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen("green_dot.png", confidence=.7)
            pt.moveTo(position[0:2],duration = self.speed)
            pt.moveRel(-100,0,duration = self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print(e)
            print("green dot not found")
            return False

    # Navigate to chatbox
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen("paperclip.png", confidence=.7)
            pt.moveTo(position[0:2],duration = self.speed)
            pt.moveRel(100,10,duration = self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print(e)
            print("Paperclip not found")
            return False

    # Send message
    def send_message(output):
        try:
            pt.typewrite(output, interval=4)
            pt.press("enter")
        except Exception as e:
            print(e)
            print("Message not sent")
            return False