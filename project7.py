from tkinter import *
from tkinter import ttk                     #combo box
from googletrans import Translator,LANGUAGES


def get1():
    source_lang = com1.get()
    target_lang = com2.get()
    get1 = sor.get(1.0, END)

    translator = Translator()
    get1 = translator.translate(get1, src=source_lang, dest=target_lang)

    sor2.delete(1.0, END)
    sor2.insert(END, get1.text) 
 
root = Tk()                         #to make obj and use to Tk():- all fun.


root.title("Translator")
root.geometry("500x700")  # Set the height and width
root.config(bg="lightblue")    # Set the background color to red


lab=Label(root,text="translator",font=("Time New Roman",20,"bold"),bg="white")
lab.place(x=100,y=40,height=50,width=300)

rame=Frame(root).pack(side=BOTTOM)

lab=Label(root,text="source",font=("Time New Roman",20,"bold"),bg="pink",fg="black")
lab.place(x=100,y=100,height=20,width=300)

sor=Text(rame,font=("Time New Roman",20,"bold"),wrap=WORD,bg="white")   #text box source
sor.place(x=10,y=130,height=150,width=480) 


com1=ttk.Combobox(rame, values=list(LANGUAGES.values()))
com1.place(x=10,y=300,height=40,width=150) 
com1.set("english")

But=Button(rame,text="Translator",relief=RAISED,command=get1) #     relief=RAISED  is 3d button
But.place(x=170,y=300,height=40,width=150) 

com2=ttk.Combobox(rame,values=list(LANGUAGES.values()))
com2.place(x=330,y=300,height=40,width=150) 
com2.set("hindi")

lab=Label(root,text="dest",font=("Time New Roman",20,"bold"),bg="pink",fg="black")
lab.place(x=100,y=360,height=20,width=300) 

sor2=Text(rame,font=("Time New Roman",20,"bold"),wrap=WORD,bg="white")
sor2.place(x=10,y=400,height=150,width=480) 



root.mainloop()
