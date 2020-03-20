#Programmer: Alexander Leones
#Project: Elderly Assistance Robot
#  uiCubbyCondensed.py 
# first semester lab prototype ui
# Nov 3, 2019
import time
from tkinter import *
import RPi.GPIO as GPIO
from functools import partial

#cubby gpio IDs
cubby1=21
cubby2=20
cubby3=16
cubby4=12
cubby1Input=26

space1=False #space 1 is initially empty etc
space2=False
space3=False
space4=False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(cubby1, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby2, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby3, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby4, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby1Input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

master = Tk()
photos = list()

photos.append(PhotoImage(file = r"/home/pi/Documents/PiFun/UI/EAR/gui/greetimg1.png"))
photos.append(PhotoImage(file = r"/home/pi/Documents/PiFun/UI/EAR/gui/greetimg2.png"))
photos.append(PhotoImage(file = r"/home/pi/Documents/PiFun/UI/EAR/gui/greetimg3.png"))
photos.append(PhotoImage(file = r"/home/pi/Documents/PiFun/UI/EAR/gui/greetimg4.png"))
master.title("Assistant Robot GUI V2")
master.geometry("800x100")

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
		photos[0].config(file = r"/home/pi/Documents/PiFun/UI/EAR/gui/greetimg1.png")
	elif spaceNum==2:
		global space2
		space = space2
		photos[1].config(file = r"/home/pi/Documents/PiFun/UI/EAR/gui/greetimg2.png")
	elif spaceNum==3:
		global space3
		space = space3
		photos[2].config(file = r"/home/pi/Documents/PiFun/UI/EAR/gui/greetimg3.png")
	elif spaceNum==4:
		global space4
		space = space4
		photos[3].config(file = r"/home/pi/Documents/PiFun/UI/EAR/gui/greetimg4.png")

	if(space==False): #if space was empty, set occupied and disable buttons
		takePic(spaceNum)
		GPIO.output(cubbyID, GPIO.HIGH) #signal storage op.
		Cubby1StoreButton.config(state='disabled') 
		Cubby2StoreButton.config(state='disabled') 
		Cubby3StoreButton.config(state='disabled') 
		Cubby4StoreButton.config(state='disabled')
		master.update()
		while not GPIO.input(cubby1Input): 
			time.sleep(0.01)
		print('enabled')
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		label.config(text = "Cubby ocupied") #Display it's full
	elif(space==True):                    #if space is occupied
		removePic(spaceNum)
		GPIO.output(cubbyID,GPIO.LOW)
		Cubby1StoreButton.config(state='disabled') 
		Cubby2StoreButton.config(state='disabled') 
		Cubby3StoreButton.config(state='disabled') 
		Cubby4StoreButton.config(state='disabled') 
		master.update()
		while not GPIO.input(cubby1Input):
			time.sleep(0.01)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		label.config(text="Cubby Empty")
	spaceTF(spaceNum)

def ExitButton():       #exit button creation
	Exitbutton = Button(master, text="Exit", command= EandD, bg='red')
	Exitbutton.grid(row=1, column=8, ipadx=10, ipady=10)

def EandD():            #clean up led during exit
	master.destroy()
	GPIO.cleanup()

def spaceTF(spaceNum):  #set if cubby is occupied or empty (T or F)
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

def takePic(spaceNum):
	if spaceNum==1:
		Cubby1StoreButton.config(image = photos[0])
	elif spaceNum==2:
		Cubby2StoreButton.config(image = photos[1])
	elif spaceNum==3:
		Cubby3StoreButton.config(image = photos[2])
	elif spaceNum==4:
		Cubby4StoreButton.config(image = photos[3])

def removePic(spaceNum):
	if spaceNum==1:
		Cubby1StoreButton.config(image = '')
	elif spaceNum==2:
		Cubby2StoreButton.config(image = '')
	elif spaceNum==3:
		Cubby3StoreButton.config(image = '')
	elif spaceNum==4:
		Cubby4StoreButton.config(image = '')


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
