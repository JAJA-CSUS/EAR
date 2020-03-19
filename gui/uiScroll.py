#!python3
#Programmer: Alexander Leones
#Project: Elderly Assistance Robot
#  uiCubbyScroll.py 
# second semester deployable prototype gui
# 3/19/20
import time
from tkinter import *
import RPi.GPIO as GPIO
from functools import partial
import subprocess

from PIL import ImageTk, Image
import pygame

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
hWOpen=False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(cubby1, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby2, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby3, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby4, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(cubby1Input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

master = Tk()

container = Frame(master)
canvas = Canvas(container)
scrollbar = Scrollbar(container, orient="horizontal", command=canvas.xview, width = 64)
scrollable_frame = Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)



photos = list()
pygame.mixer.init()

photos.append(PhotoImage(file = r"./greetimg3.png"))
photos.append(PhotoImage(file = r"./greetimg3.png"))
photos.append(PhotoImage(file = r"./greetimg3.png"))
photos.append(PhotoImage(file = r"./greetimg3.png"))

master.title("Assistant Robot GUI V2") 
master.geometry("1650x400")

Onlabel1 = Label(master, text="Cubby Empty (system start)")
#Onlabel1.grid(row=0, column=0)
Onlabel2 = Label(master, text="Cubby Empty (system start)")
#Onlabel2.grid(row=0, column=1)
Onlabel3 = Label(master, text="Cubby Empty (system start)")
#Onlabel3.grid(row=0, column=2)
Onlabel4 = Label(master, text="Cubby Empty (system start)")
#Onlabel4.grid(row=0, column=3)

def cubbyButton(spaceNum, cubbyID, label):

	if spaceNum==1:
		global space1 
		space = space1 
		if space==False:
			pygame.mixer.music.load("storingInOne.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
		else:
			pygame.mixer.music.load("1CubbyRetrieve.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
	elif spaceNum==2:
		global space2
		space = space2
		if space==False:
			pygame.mixer.music.load("2Store.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
		else:
			pygame.mixer.music.load("2CubbyRetrieve.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
	elif spaceNum==3:
		global space3
		space = space3
		if space==False:
			pygame.mixer.music.load("3rdCubbyStore.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
		else:
			pygame.mixer.music.load("3CubbyRetrieve.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
	elif spaceNum==4:
		global space4
		space = space4
		if space==False:
			pygame.mixer.music.load("4thcubbystore.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
		else:
			pygame.mixer.music.load("4CubbyRetrieve.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue

	if(space==False): #if space was empty, set occupied and disable buttons
		GPIO.output(cubbyID, GPIO.HIGH) #signal storage op.
		takePic(spaceNum)
		while not GPIO.input(cubby1Input): 
			time.sleep(0.01)
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled')
			master.update()
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		label.config(text = "Cubby ocupied") #Display it's full
	elif(space==True):                    #if space is occupied
		GPIO.output(cubbyID,GPIO.LOW)
		while not GPIO.input(cubby1Input):
			time.sleep(0.01)
			Cubby1StoreButton.config(state='disabled') 
			Cubby2StoreButton.config(state='disabled') 
			Cubby3StoreButton.config(state='disabled') 
			Cubby4StoreButton.config(state='disabled') 
			master.update()
		removePic(spaceNum)
		Cubby1StoreButton.config(state='normal')
		Cubby2StoreButton.config(state='normal')
		Cubby3StoreButton.config(state='normal')
		Cubby4StoreButton.config(state='normal') 
		master.update()
		label.config(text="Cubby Empty")
	spaceTF(spaceNum)

def ExitButton():       #exit button creation
	Exitbutton = Button(scrollable_frame, text="Exit", command= EandD, bg='red')
	Exitbutton.pack(side=LEFT)

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
		subprocess.call("./webcam.sh", shell=True)
		photos[0] = ImageTk.PhotoImage(Image.open("greetimg1.jpg"))  
		Cubby1StoreButton.config(image = photos[0])
	elif spaceNum==2:
		subprocess.call("./webcam2.sh", shell=True)
		photos[1] = ImageTk.PhotoImage(Image.open("greetimg2.jpg")) 
		Cubby2StoreButton.config(image = photos[1])
	elif spaceNum==3:
		subprocess.call("./webcam3.sh", shell=True)
		photos[2] = ImageTk.PhotoImage(Image.open("greetimg3.jpg")) 
		Cubby3StoreButton.config(image = photos[2])
	elif spaceNum==4:
		subprocess.call("./webcam4.sh", shell=True)
		photos[3] = ImageTk.PhotoImage(Image.open("greetimg4.jpg")) 
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

def create_window():
	global hWOpen
	if hWOpen==False:
		global helpWindow
		helpWindow = Toplevel(master)
		helpWindow.title("Help Page") 
		helpWindow.geometry("400x400")
		hWOpen=True
		print(hWOpen)
	else:
		helpWindow.destroy()
		hWOpen=False
		print(hWOpen)



Cubby1StoreButton = Button(scrollable_frame, text="GPIO 21 Cubby 1", command= partial(cubbyButton, 1, cubby1, Onlabel1))
Cubby1StoreButton.pack(side=LEFT)
Cubby2StoreButton = Button(scrollable_frame, text="GPIO 20 Cubby 2", command= partial(cubbyButton, 2, cubby2, Onlabel2))
Cubby2StoreButton.pack(side=LEFT)
Cubby3StoreButton = Button(scrollable_frame, text="GPIO 16 Cubby 3", command= partial(cubbyButton, 3, cubby3, Onlabel3))
Cubby3StoreButton.pack(side=LEFT)
Cubby4StoreButton = Button(scrollable_frame, text="GPIO 12 Cubby 4", command= partial(cubbyButton, 4, cubby4, Onlabel4))
Cubby4StoreButton.pack(side=LEFT)
helpButton = Button(scrollable_frame, text="Help Page", bg= 'blue', command=create_window)
helpButton.pack(side=LEFT)
ExitButton()
scrollbar.pack(side="bottom", fill="x")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(xscrollcommand=scrollbar.set)
container.pack(expand=True, fill="both")
canvas.pack(side="left", fill="both", expand=True)
master.mainloop()
