import tkinter as tk
from tkinter import ttk

window= tk.Tk()
window.title("Ulsa")
window.geometry("300x300")
ttk.Label(window, text="hola").pack()
ttk.Button(window, text="bye").pack()
ttk.Button(window,text="ok").pack()
window.mainloop()
