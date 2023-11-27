import tkinter as tk
from tkinter import ttk

class App():
    
    def __init__(self):
        
        #Creacion de propiedades
        self.window = tk.Tk()
        self.window.title("Joe’s Automotive")
        self.window.geometry("400x350")

        #Texto
        ttk.Label(self.window, text="Joe’s Automotive", font=("Arial, 20")).grid(row=0,column=0, padx=10, pady=10)
        ttk.Label(self.window, text="Joe’s Automotive performs the following \n routine maintenance services:", font=("Arial, 12")).grid(row=1,column=0, rowspan=2,
                                                                                                                                         padx=10, pady=10)
        #Check Buttons
        self.uno = tk.BooleanVar()
        self.dos = tk.BooleanVar()
        self.tres = tk.BooleanVar()
        self.cuatro = tk.BooleanVar()

        ttk.Checkbutton(self.window, text="Oil change—$26.00", variable= self.uno).grid(row=3, column=0, sticky="W", padx=10)
        ttk.Checkbutton(self.window, text="Lube job—$18.00", variable=self.dos).grid(row=4, column=0, sticky="W", padx=10)
        ttk.Checkbutton(self.window, text="Radiator flush—$30.00", variable=self.tres).grid(row=5, column=0, sticky="W", padx=10)
        ttk.Checkbutton(self.window, text="Transmission flush—$80.00", variable=self.cuatro).grid(row=6, column=0, sticky="W", padx=10)

        #Button
        ttk.Button(self.window, text="Done", command=self.calcular).grid(row=7,column=0, padx=10, pady=10, sticky="W", columnspan=2)

        #Total
        self.total = tk.StringVar()
        self.total.set("Total: ")
        ttk.Label(self.window, font=("Arial, 13"), textvariable= self.total).grid(row=8,column=0, padx=10, pady=10, sticky="W")

        #Inicia el programa
        self.window.mainloop()

    def calcular(self):
        resultado = 0

        if self.uno.get():
            resultado += 26
        if self.dos.get():
            resultado += 18
        if self.tres.get():
            resultado += 30
        if self.cuatro.get():
            resultado += 80

        self.total.set(f"Total: {resultado}")


if __name__ == '__main__':
    App()