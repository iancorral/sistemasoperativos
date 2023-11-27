import tkinter as tk
from tkinter import ttk

w= tk.Tk()
w.title("Ulsa")
w.geometry("300x300")
ttk.Label(w, text="Hola").grid(column=0,row=0)
ttk.Label(w,text="Ulsa").grid(column=1,row=0)
ttk.Button(w,text="Aceptar").grid(column=0,row=1)
w.mainloop()
