import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Ulsa")
        self.window.geometry("300x500")
        
        ttk.Button(self.window, text="Boton 1").grid(column=0,row=0, ipady=20)
        ttk.Button(self.window, text="Boton 2").grid(column=1,row=1)
        ttk.Button(self.window, text="Boton 4").grid(column=0,row=2)
        ttk.Button(self.window, text="Boton 3").grid(column=1,row=2,pady=20)
        ttk.Button(self.window, text="Boton 6").grid(column=0,row=3, columnspan=2)
        
        self.window.mainloop()




if __name__=='__main__':
    app= App()
