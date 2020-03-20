#Programmer: Alexander Leones
#Project: Elderly Assistance Robot
#  uiCubby.py 
# first semester lab prototype ui
# Nov 3, 2019
import time
import tkinter as tk
from tkinter.ttk import *
import RPi.GPIO as GPIO

#cubby gpio IDs
cubby1=21
cubby2=20
cubby3=16
cubby4=12
cubby1Input=26

space1=False #space 1 is initially empty
space2=False
space3=False
space4=False

GPIO.setmode(GPIO.BCM)
GPIO.setup(cubby1, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby2, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby3, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby4, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby1Input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
master = tk.Tk()
master.title("Assistant Robot GUI V2")
master.geometry("600x100")

ONlabel1 = tk.Label(master, text="Cubby Empty (system start)", font=30)
ONlabel1.grid(row=0, column=1 ,pady=20)
ONlabel2 = tk.Label(master, text="Cubby Empty (system start)", font=30)
ONlabel2.grid(row=1, column=1, pady=20)
ONlabel3 = tk.Label(master, text="Cubby Empty (system start)", font=30)
ONlabel3.grid(row=2, column=1, pady=20)
ONlabel4 = tk.Label(master, text="Cubby Empty (system start)", font=30)
ONlabel4.grid(row=3, column=1, pady=20)

def cubby1Button():
	global space1
	if(space1==False):
		GPIO.output(cubby1, GPIO.HIGH) #signal storage output.
		while not GPIO.input(cubby1Input):
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled')
			master.update()
			time.sleep(0.1)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		space1=True           #space1 is occupied? True
		ONlabel1.config(text = "Cubby ocupied") #Display it's full
	else:
		GPIO.output(cubby1,GPIO.LOW)
		while not GPIO.input(cubby1Input):
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled') 
			master.update()
			time.sleep(0.1)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		space1=False
		ONlabel1.config(text="Cubby Empty")	

def cubby2Button():
	global space2
	if(space2==False):
		GPIO.output(cubby2, GPIO.HIGH) #signal storage op.
		while not GPIO.input(cubby1Input):
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled') 
			master.update()
			time.sleep(0.1)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		space2=True           #space1 is occupied? True
		ONlabel2.config(text = "Cubby ocupied") #Display it's full
	else:
		GPIO.output(cubby2,GPIO.LOW)
		while not GPIO.input(cubby1Input):
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled') 
			master.update()
			time.sleep(0.1)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		space2=False
		ONlabel2.config(text="Cubby Empty")

def cubby3Button():
	global space3
	if(space3==False):
		GPIO.output(cubby3, GPIO.HIGH)
		while not GPIO.input(cubby1Input):
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled') 
			master.update()
			time.sleep(0.1)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		space3=True
		ONlabel3.config(text = "Cubby ocupied") #Display it's full
	else:
		GPIO.output(cubby3, GPIO.LOW)
		while not GPIO.input(cubby1Input):
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled') 
			master.update()
			time.sleep(0.1)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		space3=False
		ONlabel3.config(text="Cubby Empty")
def cubby4Button():
	global space4
	if(space4==False):
		GPIO.output(cubby4, GPIO.HIGH) #signal storage op.
		while not GPIO.input(cubby1Input):
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled') 
			master.update()
			time.sleep(0.1)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		space4=True           #space1 is occupied? True
		ONlabel4.config(text = "Cubby ocupied") #Display it's full
	else:
		GPIO.output(cubby4,GPIO.LOW)
		while not GPIO.input(cubby1Input):
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled') 
			master.update()
			time.sleep(0.1)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		space4=False
		ONlabel4.config(text="Cubby Empty")



def ExitButton():
	Exitbutton = tk.Button(master, text="Exit", command= EandD, bg='red')
	Exitbutton.grid(row=0, column=2, padx=10, ipadx=20, ipady=10)
def EandD():
	master.destroy()
	GPIO.cleanup()

Cubby1StoreButton = tk.Button(master, text="GPIO 21 Cubby 1", font=("Courier", 30), command=cubby1Button)
Cubby1StoreButton.grid(row=0, column=0, ipadx=50, ipady=20)
Cubby2StoreButton = tk.Button(master, text="GPIO 20 Cubby 2", font=("Courier", 30), command=cubby2Button)
Cubby2StoreButton.grid(row=1, column=0, ipadx=50, ipady=20)
Cubby3StoreButton = tk.Button(master, text="GPIO 16 Cubby 3", font=("Courier", 30), command=cubby3Button)
Cubby3StoreButton.grid(row=2, column=0, ipadx=50, ipady=20)
Cubby4StoreButton = tk.Button(master, text="GPIO 12 Cubby 4", font=("Courier", 30), command=cubby4Button)
Cubby4StoreButton.grid(row=3, column=0, ipadx=50, ipady=20)
ExitButton()

master.mainloop()
