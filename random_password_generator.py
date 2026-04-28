import tkinter as tk
from tkinter import messagebox
import json
import random

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("500x500")

alphabet = "abcdefghijklmnopqrstuvwyz"
numbers = "0123456789"
special = "~`!@#$%^&*()-_+=|/.,<>№;:?[]{}"

lb = tk.Listbox(window, height=10,width=50)
lb.pack()

length = tk.Label(window, text="Длина пароля: 3")
length.pack(pady=10)

def update_length(scrol):
   length.config(text=f"Длина пароля: {scrol}")

sb = tk.Scale(window,from_= 3,to=30,orient='horizontal',length=300,command=update_length)

sb.pack()

a = tk.IntVar()
b = tk.IntVar()
c = tk.IntVar()
d = tk.IntVar()
acb = tk.Checkbutton(text="буквы", variable = a)
acb.pack()
upprcase = tk.Checkbutton(text="Заглавные буквы", variable = b)
upprcase.pack()
num = tk.Checkbutton(text="цифры", variable = c)
num.pack()
spc = tk.Checkbutton(text="особые знаки", variable = d)
spc.pack()

def load():
   try:
       with open("passwords.json", "r", encoding="utf-8") as file:
           return json.load(file)
   except (FileNotFoundError, json.JSONDecodeError):
       return []

pws = load()

def save(pws):
    with open("passwords.json", "w+",encoding="utf-8") as file:
        json.dump(pws, file, ensure_ascii=False, indent=4)


def update_listbox():
   lb.delete(0, tk.END)
   for p in range(len(pws)-1,0,-1):
       lb.insert(tk.END, pws[p])

update_listbox()

def add():
   global pws, a, b, c, d

   slop = ""
   if a.get():
      slop += alphabet
   if b.get():
      slop += alphabet.upper()
   if c.get():
      slop += numbers
   if d.get():
      slop += special
   
   
   if len(slop) > 0:
      text = ""
      for i in range(sb.get()):
         text += slop[random.randint(0, len(slop)-1)]
      pws.append(text)
      update_listbox()
      save(pws)
    
button = tk.Button(window, width=30, height=2, text="Сгенерировать пароль", command=add).pack()


