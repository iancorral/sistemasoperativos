import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("IMC")

        # Titulo
        ttk.Label(self.window, text="IMC", 
            font=("Arial", 20), foreground="blue").grid(column=1,row=0)        
        
        # Peso
        ttk.Label(self.window, text="Peso:").grid(column=0, row=1)
        self.peso = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.peso).grid(column=1, 
                                                            row=1)

        # Altura
        ttk.Label(self.window, text="Altura:").grid(column=0, row=2)
        self.altura = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.altura).grid(column=1, 
                                                            row=2)
        
        # Botón calcular
        ttk.Button(self.window, text="Calcular", 
                   command=self.calcular).grid(column=0, row=3, 
                                          columnspan=2, sticky="WE")
        
        # Resultado
        self.resultado = tk.StringVar()
        self.resultado.set("imc = ")
        ttk.Label(self.window, 
                  textvariable=self.resultado).grid(column=1, row=4)

        # Imagen
        self.photo = tk.PhotoImage(file="./img/imc_normal.png")
        ttk.Label(self.window, image=self.photo).grid(column=2, row=1, 
                                                 rowspan=4)

        self.window.mainloop()

    def calcular(self):
        peso = self.peso.get()
        altura = self.altura.get()
        imc = peso / altura**2
        self.resultado.set(f"imc = {imc:.2f}")
        self.photo.configure(file="./img/dado1.png")

if __name__ == '__main__':
    App()
