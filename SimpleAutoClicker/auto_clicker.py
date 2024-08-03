from tkinter import *
import time
from pynput.mouse import Controller
from pynput.mouse import Button as btn

window = Tk()
window.title("Auto Clicker")
mouse = Controller()


def get_position():
	global position
	time.sleep(3)
	position = mouse.position
	Label(window, text=position).grid(column=0, row=1)


def left_click():
	global mouse_button_type
	mouse_button_type = 'left'
	Button(window, text="Left click", cursor="hand2", bg='green',
		   command=lambda: left_click()).grid(column=0, row=2)
	Button(window, text="Right click", cursor="hand2", bg='red',
		   command=lambda: right_click()).grid(column=1, row=2)


def right_click():
	global mouse_button_type
	mouse_button_type = 'right'
	Button(window, text="Right click", cursor="hand2", bg='green',
		   command=lambda: right_click()).grid(column=1, row=2)
	Button(window, text="Left click", cursor="hand2", bg='red',
		   command=lambda: left_click()).grid(column=0, row=2)


def start():
	mouse.position=(0,0)
	amount = amount_entry.get()
	amount = int(amount)
	delay = delay_entry.get()
	delay = float(delay)
	mouse.move(position[0], position[1])
	if amount != 0:
		for i in range(amount):
			time.sleep(delay)
			if mouse_button_type == 'left':
				mouse.click(btn.left, 1)
			elif mouse_button_type == 'right':
				mouse.click(btn.right, 1)
			else:
				break
	else:
		while True:
			time.sleep(delay)
			if mouse_button_type == 'left':
				mouse.click(btn.left, 1)
			elif mouse_button_type == 'right':
				mouse.click(btn.right, 1)
			else:
				break


Label(window, text="Delay").grid(column=1, row=0)
delay_entry = Entry(window, width=20)
delay_entry.grid(column=0, row=0)


Button(window, text="Cords", command=lambda: get_position(),
	   cursor="hand2").grid(column=1, row=1)


Button(window, text="Left click", cursor="hand2", bg='red',
	   command=lambda: left_click()).grid(column=0, row=2)
Button(window, text="Right click", cursor="hand2", bg='red',
	   command=lambda: right_click()).grid(column=1, row=2)


Label(window, text="Nr. of clicks").grid(column=1, row=3)
amount_entry = Entry(window, width=20)
amount_entry.grid(column=0, row=3)


Button(window, text="Start", command=lambda: start(),
	   cursor="hand2").grid(column=0, row=4)


window.mainloop()
