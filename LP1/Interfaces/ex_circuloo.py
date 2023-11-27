import tkinter as tk
from tkinter import ttk
import math

class App:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Círculo")
        
        #imagen
        photo=tk.PhotoImage(file="./img/nose.png")
        ttk.Label(self.window,image=photo).grid(column=1,row=1,pady=10,columnspan=10,ipadx=20)
        
        #ULSA
        ttk.Label(self.window, text="Calculadora", font="Arial, 30", foreground="Blue").grid(column=0,row=0, columnspan=2, pady=10)
        
        #Introducir radio
        ttk.Label(self.window, text="Introducir radio").grid(column=0,row=1, padx=10)
        self.radio = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.radio).grid(column=0, row=2)
        
        #Mostrar resultado
        self.resultado = tk.StringVar()
        self.resultado.set("El área es: ")
        ttk.Label(self.window,  textvariable=self.resultado).grid(column=0,row=3, pady= 10, sticky="W",padx=10)
        
        #Botons
        ttk.Button(self.window, text= "Calcular", command=self.calcular).grid(column=0,row=4, sticky="WE", padx=10, pady=10, columnspan=2)
        
        self.window.mainloop()
        
    def calcular(self):
        radio=self.radio.get()
        resultado = round((math.pi)*((radio)**2),2)
        self.resultado.set(f"El área es = {resultado}")
        
        
if __name__ == '__main__':
    app = App()
    
        