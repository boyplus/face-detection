import os
import os, os.path
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
gender = ""
age = 0

ageRange = ["0-2","4-6","8-12","15-20","25-32","38-43"]
numberMaleImage = []
numberFemaleImage = []
# set the number of image od male and female to 0 for every ageRange
for i in range(len(ageRange)):
    numberMaleImage.append(0)
    numberFemaleImage.append(0)

# count the number of male and female image in directory
for i in range (len(ageRange)):
    DIR = "./"+"Male/"+ageRange[i]
    numberMaleImage[i] = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    DIR = "./"+"Female/"+ageRange[i]
    numberFemaleImage[i] = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

# print the number of image that we found
for i in range(len(ageRange)):
    print("Male   "+ageRange[i]+" has "+str(numberMaleImage[i])+" pictures")
    print("Female "+ageRange[i]+" has "+str(numberFemaleImage[i])+" pictures")


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
    global panel,img,btnRandom,hair,displayHair,gender,ansGender,age,ageRange,numberMaleImage
    if(displayHair != None):
        displayHair.destroy()
    
    for i in range (len(ageRange)):
        if(age == ageRange[i]):
            theSize = numberMaleImage[i]
            break
    print("number is"+str(theSize))
    num = random.randint(1,theSize)
    print("num = "+str(num))
    path = "./"+gender+"/"+age+"/"+str(num)+".jpg"
    print(path)

    hair = Image.open(path)
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
    global img,panel,btnRandom,genderTetx,gender,age,ageText,ansGender
    res()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    
    s = "python gad.py --image "
    s = s+x
    os.system(s)
    f = open("gender.txt","r")
    gender = f.read()
    f.close()
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
        f.close()
        ageText = tkinter.Label(root, text=age)
        ageText.pack()
        btnRandom = Button(root, text='Random', command=callBack)
        btnRandom.pack()

btn = tkinter.Button(root, text='choose picture', command=open_img).pack()

root.mainloop()
