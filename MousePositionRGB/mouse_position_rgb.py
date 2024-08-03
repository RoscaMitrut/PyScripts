from PIL import ImageGrab
from pynput.mouse import Controller
from time import sleep

mouse = Controller()

for _ in range(5):
	position = mouse.position
	print(position)
	
	im2 = ImageGrab.grab()
	print(im2.getpixel((position[0], position[1])),"\n")

	sleep(1)