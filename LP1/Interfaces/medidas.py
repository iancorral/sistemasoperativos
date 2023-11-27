import tkinter as tk
from tkinter import ttk

class App():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora de medidas")
        self.window.geometry("300x200")

        #Metros
        ttk.Label(self.window, text="Metros", font=("Arial, 12")).grid(row=0, column=0, padx=20, columnspan=5, sticky="W")

        #Entry
        self.metros = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.metros).grid(row=1, column=0, padx=20)
         
        #Boton
        ttk.Button(self.window, text="Calcular", command=self.calcular).grid(row=1, column=1)

        #Radio buttons
        self.tipo = tk.StringVar()
        ttk.Label(self.window, text="    Convertir a:", font=("Arial, 12")).grid(column=0,row=4, sticky="W")
        ttk.Radiobutton(self.window, text='Yardas', variable=self.tipo, value='yardas').grid(column=0,row=5, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text='Pies', variable=self.tipo, value='pies').grid(column=0,row=6, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text='Pulgadas', variable=self.tipo, value='pulgadas').grid(column=0,row=7, sticky="W", padx=20)

        #Resultado
        self.resutlado = tk.StringVar()
        self.resutlado.set("Resultado")
        ttk.Label(self.window, textvariable=self.resutlado, font=("Arial, 12")).grid(row=8, column=0, padx=20, pady=10)

        self.window.mainloop()

    def calcular(self):
        var = self.metros.get()
        tipo = self.tipo.get()

        if tipo == "yardas":
            res = var*1.09
        if tipo == "pies":
            res = var*3.28
        if tipo == "pulgadas":
            res = var*39.37

        self.resutlado.set(f"Resultado: {round(res, 2)}")
        
if __name__ == '__main__':
    App()