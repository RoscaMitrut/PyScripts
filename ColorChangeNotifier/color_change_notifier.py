from PIL import Image, ImageGrab
from pynput.mouse import Button, Controller
from time import sleep
from playsound import playsound
import multiprocessing 

def color_checker(position,color1):
	while True:
		im2 = ImageGrab.grab()
		color2 = im2.getpixel((position[0], position[1]))
		if color2 != color1:
			playsound('tick.mp3')
		else:
			sleep(5)

if __name__ == '__main__':
	mouse = Controller()

	print('Move your mouse')
	sleep(2)
	position = mouse.position
	print(position)
	im1 = ImageGrab.grab()
	color1 = im1.getpixel((position[0], position[1]))
	print(color1)
	print('Location and color saved')
	
	p1 = multiprocessing.Process(target=color_checker,args=(position,color1))
	p1.start()
	input()
	p1.terminate()