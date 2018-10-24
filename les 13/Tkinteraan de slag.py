from tkinter import *
import requests
import xmltodict

def click():
    keuze = entry.get



root = Tk()

label = Label(master=root,text="Voer een station in",height=2)
label.pack()

entry = Entry(master=root)
entry.pack(pady=10)

button = Button(master=root, text="Station invoeren", command=click())
button.pack(padx=10, pady=10)

root.mainloop()