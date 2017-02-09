import RPi.GPIO as gpio
import Tkinter as tk
import time

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(7,gpio.OUT)
	gpio.setup(11,gpio.OUT)
	gpio.setup(13,gpio.OUT)
	gpio.setup(15,gpio.OUT)

def fwd(tf):
	gpio.output(7,True)
	gpio.output(11,False)
	gpio.output(15,True)
	gpio.output(13,False)
	time.sleep(tf)
	gpio.cleanup()

def back(tf):
	gpio.output(7,False)
	gpio.output(11,True)
	gpio.output(15,False)
	gpio.output(13,True)
	time.sleep(tf)
	gpio.cleanup()

def left(tf):
	gpio.output(7,True)
	gpio.output(11,False)
	gpio.output(15,False)
	gpio.output(13,False)
	time.sleep(tf)
	gpio.cleanup()

def right(tf):
	gpio.output(7,False)
	gpio.output(11,False)
	gpio.output(15,True)
	gpio.output(13,False)
	time.sleep(tf)
	gpio.cleanup()

def key_input(event):
	init()
	key_press = event.char
	print(key_press)
	sleep_time = 0.15
	

	if(key_press.lower()=='w'):	
		fwd(sleep_time)
	if(key_press.lower()=='a'):
		left(sleep_time)
	if(key_press.lower()=='d'):
		right(sleep_time)
	if(key_press.lower()=='s'):
		back(sleep_time)

command = tk.Tk()
command.bind('<KeyPress>',key_input)
command.mainloop()
