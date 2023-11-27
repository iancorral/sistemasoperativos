import tkinter as tk
from tkinter import ttk

window= tk.Tk()
window.title("Ulsa")
window.geometry("300x200")

ttk.Label(window,text="hola").grid(column=0,row=0)
ttk.Button(window,text="ok").grid(column=0,row=1)
ttk.Button(window,text="aceptar").grid(column=0,row=2)

photo=tk.PhotoImage(file="./img/nose.png")
ttk.Label(window,image=photo).grid(column=0, row=3)

window.mainloop()