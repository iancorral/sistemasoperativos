import tkinter as tk
from tkinter import ttk

# Calcula coste de viaje con validación y cálculo posterior

class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Alta Velocidad")

        #Imagen
        tren = tk.PhotoImage(file='./img/tren-128x64.png')   
        ttk.Label(self.window, image=tren).grid(column=0,row=0)

        # Número de viajeros
        ttk.Label(self.window, text="Viajeros:").grid(column=0,row=1, sticky="W")                               
        self.num_via = tk.IntVar(value=1)
        tk.Spinbox(self.window, from_=1, to=20, wrap=True, textvariable=self.num_via, state='readonly').grid(column=0,row=2, padx=20)
        
        # Checkbutton (Ida y Vuelta)
        self.ida_vue = tk.BooleanVar()        
        ttk.Checkbutton(self.window, text='Ida y vuelta',variable=self.ida_vue,onvalue=True, offvalue=False).grid(column=0,row=3, sticky="W")
        
        # Radiobutton (Clase de boleto)
        self.clase   = tk.StringVar(value='t')
        ttk.Label(self.window, text="Clase:").grid(column=0,row=4, sticky="W")
        ttk.Radiobutton(self.window, text='Turista', variable=self.clase, value='t').grid(column=0,row=5, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text='Primera', variable=self.clase, value='p').grid(column=0,row=6, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text='Lujo', variable=self.clase, value='l').grid(column=0,row=7, sticky="W", padx=20)        
        
        # Entry (Distancia)
        ttk.Label(self.window, text="Distancia Kilómetros):").grid(column=0,row=8, sticky="W")
        self.km = tk.IntVar(value=10)        
        ttk.Entry(self.window, textvariable=self.km, width=10).grid(column=0,row=9, sticky="W", padx=20)
        
        # Entry (Precio)
        self.precio = tk.DoubleVar(value=1)
        ttk.Label(self.window, text="Precio:").grid(column=0,row=10, sticky="W")
        ttk.Entry(self.window, textvariable=self.precio, width=10).grid(column=0,row=11, sticky="W", padx=20)        
        
        # Label (Mostrar resultado)
        self.total = tk.DoubleVar(value=0)
        ttk.Label(self.window, text="A Pagar (euros):").grid(column=0,row=12, sticky="W")        
        ttk.Label(self.window, textvariable=self.total,foreground="yellow", background="black",borderwidth=5, anchor="e").grid(column=0,row=13)             
                       
        # Botones
        ttk.Button(self.window, text="Calcular", command=self.calcular).grid(column=0,row=15, sticky="WE", padx=10)
        ttk.Button(self.window, text="Salir", command=quit).grid(column=0, row=16, sticky="WE", padx=10)

        self.window.mainloop()
        
    def calcular(self):        
        total = 0
        km = int(self.km.get())
        precio = float(self.precio.get())
        total =  self.num_via.get() * km * precio
        
        if self.ida_vue.get():
            total = total * 1.5

        if self.clase.get() == 'p':
            total = total * 1.2
        elif self.clase.get() == 'l':
            total = total * 2

        self.total.set(total)                


if __name__ == '__main__':
    App()
