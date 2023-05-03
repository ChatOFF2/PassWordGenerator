import tkinter
import pyperclip
import random
from tkinter import messagebox
import json


def passwordgen():
    little_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
    allsymbols=[little_letters,upper_letters,symbols]
    new_word=""
    for i in range (20):
        randomlist=random.choice(allsymbols)
        randomsymbol=random.choice(randomlist)
        new_word+=randomsymbol
    entrypassword.delete(0, 999)
    entrypassword.insert(0,new_word)
    pyperclip.copy(new_word)

def addcomand():
    try:
        with open("myjson.json",mode="r") as file:
            mydict = json.load(file)
    except FileNotFoundError:
        with open("myjson.json",mode="w") as file:
            mydict={entrynamesite.get():{"mail":entrymailorname.get(),"passw":entrypassword.get()}}
            json.dump(mydict,file)
    else:
        mydict[entrynamesite.get()] = {"mail": entrymailorname.get(), "passw": entrypassword.get()}
        with open("myjson.json", mode="w") as file2:
            json.dump(mydict,file2)

    messagebox.showinfo(title="Инфо", message="данные сохранены")
    pyperclip.copy(entrypassword.get())

def searchcommand():
    try:
        with open("myjson.json", mode="r") as file:
            mydict=json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Нет файла","Файл на пк не создан")
    else:
        if entrynamesite.get() in mydict:
            entrymailorname.delete(0,999)
            entrymailorname.insert(0,mydict[entrynamesite.get()]["mail"])
            entrypassword.delete(0,999)
            entrypassword.insert(0,mydict[entrynamesite.get()]["passw"])
        else:
            messagebox.showerror("Нет записи", "Нет ни одной записи для поиска")


window = tkinter.Tk()
window.title("PassWordGen")

window.config(height=250, width=250,padx=30)

image=tkinter.PhotoImage(file="locker 1.png")
canvas=tkinter.Canvas(height=75, width=75)
canvas.config(highlightthickness=0)
canvas.create_image(37,37,image=image)
canvas.grid(row=0,column=1,pady=15)

labelnamesite=tkinter.Label(text="Название сайта:")
labelnamesite.grid(row=1,column=0)

entrynamesite=tkinter.Entry(width=35)
entrynamesite.grid(row=1,column=1)

labelmailorname=tkinter.Label(text="Имя пользователя/или е-майл:")
labelmailorname.grid(row=2,column=0,padx=20,pady=5)

entrymailorname=tkinter.Entry(width=50)
entrymailorname.grid(row=2,column=1,columnspan=2,sticky="w")
entrymailorname.insert(0,"mail@mail.ru")

labelpassword=tkinter.Label(text="Password")
labelpassword.grid(row=3,column=0)

entrypassword=tkinter.Entry(width=35)
entrypassword.grid(row=3,column=1,sticky="W")

battungenerate=tkinter.Button(text="Generate Pass",command=passwordgen)
battungenerate.grid(row=3,column=2,sticky="E")

battunadd=tkinter.Button(text="Add",width=40,command=addcomand)
battunadd.grid(row=4,columnspan=3,pady=7)

battunsearch=tkinter.Button(text="Search",width=11,command=searchcommand)
battunsearch.grid(row=1,column=2,sticky="E")







window.mainloop()
