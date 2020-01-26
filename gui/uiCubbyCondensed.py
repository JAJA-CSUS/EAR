#Programmer: Alexander Leones
#Project: Elderly Assistance Robot
#  uiCubbyCondensed.py 
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

ONlabel1 = Label(master, text="Cubby Empty (system start)")
ONlabel1.grid(row=0, column=0)
ONlabel2 = Label(master, text="Cubby Empty (system start)")
ONlabel2.grid(row=0, column=1)
ONlabel3 = Label(master, text="Cubby Empty (system start)")
ONlabel3.grid(row=0, column=2)
ONlabel4 = Label(master, text="Cubby Empty (system start)")
ONlabel4.grid(row=0, column=3)


def cubbyButton(space, cubbyID, label):
	
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
		space=True           #space1 is occupied? True
		label.config(text = "Cubby ocupied") #Display it's full
	else:
		GPIO.output(cuubyID,GPIO.LOW)
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
		space=False
		label.config(text="Cubby Empty")



def ExitButton():
	Exitbutton = tk.Button(master, text="Exit", command= EandD, bg='red')
	Exitbutton.grid(row=1, column=8, ipadx=10, ipady=10)
def EandD():
	master.destroy()
	GPIO.cleanup()

Cubby1StoreButton = Button(master, text="GPIO 21 Cubby 1", command=cubbyButton(space1, cubby1, Onlabel1))
Cubby1StoreButton.grid(row=1, column=0, ipadx=20, ipady=20)
Cubby2StoreButton = Button(master, text="GPIO 20 Cubby 2", command=cubbyButton(space2, cubby2, Onlabel2))
Cubby2StoreButton.grid(row=1, column=1, ipadx=20, ipady=20)
Cubby2StoreButton = Button(master, text="GPIO 20 Cubby 3", command=cubbyButton(space3, cubby3, Onlabel3))
Cubby3StoreButton.grid(row=1, column=2, ipadx=20, ipady=20)
Cubby2StoreButton = Button(master, text="GPIO 20 Cubby 4", command=cubbyButton(space4, cubby4, Onlabel4))
Cubby4StoreButton.grid(row=1, column=3, ipadx=20, ipady=20)
ExitButton()

master.mainloop()
