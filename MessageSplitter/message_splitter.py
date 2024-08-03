from pyautogui import press, typewrite
from time import sleep

message = """
text text text
"""

split_message = message.split()

sleep(2)

for i in split_message:
	typewrite(i)
	press('enter')#"enter"
	sleep(0.2)