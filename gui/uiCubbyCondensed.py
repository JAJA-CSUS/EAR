#Programmer: Alexander Leones
#Project: Elderly Assistance Robot
#  uiCubbyCondensed.py 
# first semester lab prototype ui
# Nov 3, 2019
import time
import tkinter as tk
from tkinter.ttk import *
import RPi.GPIO as GPIO
from functools import partial
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

Onlabel1 = Label(master, text="Cubby Empty (system start)")
Onlabel1.grid(row=0, column=0)
Onlabel2 = Label(master, text="Cubby Empty (system start)")
Onlabel2.grid(row=0, column=1)
Onlabel3 = Label(master, text="Cubby Empty (system start)")
Onlabel3.grid(row=0, column=2)
Onlabel4 = Label(master, text="Cubby Empty (system start)")
Onlabel4.grid(row=0, column=3)

def cubbyButton(spaceNum, cubbyID, label):
	if spaceNum==1:
		global space1 
		space = space1
	elif spaceNum==2:
		global space2
		space = space2
	elif spaceNum==3:
		global space3
		space = space3
	elif spaceNum==4:
		global space4
		space = space4
	if(space==False):
		GPIO.output(cubbyID, GPIO.HIGH) #signal storage op.
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
		#space=True           #space1 is occupied? True
		spaceTF(spaceNum)
		label.config(text = "Cubby ocupied") #Display it's full
	else:
		GPIO.output(cubbyID,GPIO.LOW)
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
		#space=False
		spaceTF(spaceNum)
		label.config(text="Cubby Empty")

		
def ExitButton():
	Exitbutton = tk.Button(master, text="Exit", command= EandD, bg='red')
	Exitbutton.grid(row=1, column=8, ipadx=10, ipady=10)
def EandD():
	master.destroy()
	GPIO.cleanup()
def spaceTF(spaceNum):
	if spaceNum==1:
		global space1 
		space1= not space1
	elif spaceNum==2:
		global space2 
		space2= not space2
	elif spaceNum==3:
		global space3 
		space3= not space3
	elif spaceNum==4:
		global space4 
		space4= not space4
Cubby1StoreButton = Button(master, text="GPIO 21 Cubby 1", command= partial(cubbyButton, 1, cubby1, Onlabel1))
Cubby1StoreButton.grid(row=1, column=0, ipadx=20, ipady=20)
Cubby2StoreButton = Button(master, text="GPIO 20 Cubby 2", command= partial(cubbyButton, 2, cubby2, Onlabel2))
Cubby2StoreButton.grid(row=1, column=1, ipadx=20, ipady=20)
Cubby3StoreButton = Button(master, text="GPIO 20 Cubby 3", command= partial(cubbyButton, 3, cubby3, Onlabel3))
Cubby3StoreButton.grid(row=1, column=2, ipadx=20, ipady=20)
Cubby4StoreButton = Button(master, text="GPIO 20 Cubby 4", command= partial(cubbyButton, 4, cubby4, Onlabel4))
Cubby4StoreButton.grid(row=1, column=3, ipadx=20, ipady=20)
ExitButton()

master.mainloop()
