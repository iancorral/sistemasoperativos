import tkinter as tk
from tkinter import ttk
import math

class App:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("IMC")
        
        #titulo
        ttk.Label(self.window, text="IMC", font="Arial, 20").grid(column=1,row=0, columnspan=2, pady=10)
        
        #peso
        ttk.Label(self.window, text="Peso: ").grid(column=0,row=1)
        self.peso=tk.DoubleVar()
        ttk.Entry(self.window,textvariable=self.peso).grid(column=1,row=1)
        
        #altura
        ttk.Label(self.window, text="Altura: ").grid(column=0,row=2)
        self.altura=tk.DoubleVar()
        ttk.Entry(self.window,textvariable=self.altura).grid(column=1,row=2)
        
        #Boton
        ttk.Button(self.window, text= "Calcular", command=self.calcular).grid(column=0,row=3, sticky="WE", padx=10, pady=10, columnspan=2)
        
        #Resultado
        self.resultado=tk.StringVar()
        self.resultado.set("IMC: ")
        ttk.Label(self.window,textvariable=self.resultado).grid(column=1,row=4)
        
        #imagen
        self.photo=tk.PhotoImage(file="./img/nose.png")
        ttk.Label(self.window,image=self.photo).grid(column=2,row=1,rowspan=4)
    
    
        self.window.mainloop()
        
    def calcular(self):
        peso=self.peso.get()
        altura=self.altura.get()
        imc=peso/altura**2
        self.resultado.set(f"IMC= {imc:.2f}")
        self.photo.configure(file="./img/carro2.png")
        
        
               
if __name__=="__main__":
    App()