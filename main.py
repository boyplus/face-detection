import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import tkinter
import random 



root = Tk()
root.geometry("800x600")
root.resizable(width=True, height=True)
img = None
panel = None
btnRandom = None
displayHair = None
genderTetx = None
ageText = None
def res():
	global panel,img,btnRandom,displayHair,genderTetx,ageText
	if(displayHair != None):
		displayHair.destroy()
	if(panel != None):
		panel.destroy()
	if(btnRandom != None):
		btnRandom.destroy()
	if(genderTetx != None):
		genderTetx.destroy()
	if(ageText != None):
		ageText.destroy()

def callBack():
	global panel,img,btnRandom,hair,displayHair
	if(displayHair != None):
		displayHair.destroy()

	num = random.randint(1,4)
	x = "style"+str(num)+".jpg"
	hair = Image.open(x)
	hair = hair.resize((250,250),Image.ANTIALIAS)
	hair = ImageTk.PhotoImage(hair)
	displayHair = Label(root,image=hair)
	displayHair.image = hair
	displayHair.pack()

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    # print(x)
    global img,panel,btnRandom,genderTetx,ageText
    res()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    btnRandom = Button(root, text='Random', command=callBack)
    btnRandom.pack()
    s = "python gad.py --image "
    s = s+x
    os.system(s)
    f = open("gender.txt","r")
    gender = f.read()
    ansGender = ""
    if(gender == "No face detected"):
    	ansGender = gender
    else:
    	ansGender="You are "+gender
    genderTetx = tkinter.Label(root, text=ansGender+"!")
    genderTetx.pack()

    if(gender != "No face detected"):	
    	f = open("age.txt","r")
    	age = f.read()
    	ageText = tkinter.Label(root, text=age)
    	ageText.pack()

btn = tkinter.Button(root, text='choose picture', command=open_img).pack()

root.mainloop()
