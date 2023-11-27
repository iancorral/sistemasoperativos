import tkinter as tk
from tkinter import ttk
import random

class App :

    def __init__ (self) :

        self.window = tk.Tk ()
        self.window.title ("ROLL THE DICE")

        #IMAGEN
        self.photo1 = tk.PhotoImage (file = "./img/dado1.png")
        ttk.Label (self.window, image = self.photo1).grid (column = 0, row = 1)

        #IMAGEN
        self.photo2 = tk.PhotoImage (file = "./img/dado1.png")
        ttk.Label (self.window, image = self.photo2).grid (column = 1, row = 1)

        #BOTON
        ttk.Button (self.window, text = "LANZAR", command = self.calcular).grid (column = 0, row =2 , columnspan = 2)
    
        self.window.mainloop ()

    def calcular (self) :
        dado1 = random.randint (1,6)
        dado2 = random.randint (1,6)

        self.photo1.configure (file = f"./img/dado{dado1}.png")
        self.photo2.configure (file = f"./img/dado{dado2}.png")

if __name__ == '__main__':
    App ()