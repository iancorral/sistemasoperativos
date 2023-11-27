import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Taller Automotriz")
        
        # Checkbutton (Cambio de aceite)
        self.aceite = tk.BooleanVar()        
        ttk.Checkbutton(self.window, text='Cambio de aceite: $100',variable=self.aceite,onvalue=True, offvalue=False).grid(column=0,row=0, sticky="W")
        
        # Checkbutton (Rotación)
        self.rotacion = tk.BooleanVar()        
        ttk.Checkbutton(self.window, text='Rotación: $200',variable=self.rotacion,onvalue=True, offvalue=False).grid(column=0,row=1, sticky="W")
        
        # Checkbutton (Anticongelante)
        self.anti = tk.BooleanVar()        
        ttk.Checkbutton(self.window, text='Anticongelante: $150',variable=self.anti,onvalue=True, offvalue=False).grid(column=0,row=2, sticky="W")
        
        #Label (Otros servicios)
        ttk.Label(self.window,text="Otros servicios").grid(column=0,row=3,sticky="W")
        
        # Entry (Horas)
        ttk.Label(self.window, text="Horas:").grid(column=0,row=4, sticky="W")
        self.hr = tk.IntVar(value=0)        
        ttk.Entry(self.window, textvariable=self.hr, width=10).grid(column=1,row=4, sticky="W", padx=5)
        
        # Entry (Costo Refacciones)
        self.ref = tk.DoubleVar(value=0)
        ttk.Label(self.window, text="Costo Refacciones:").grid(column=0,row=5, sticky="W")
        ttk.Entry(self.window, textvariable=self.ref, width=10).grid(column=1,row=5, sticky="W", padx=5)        
        
        # Label (Mostrar resultado)
        self.total = tk.DoubleVar(value=0)
        ttk.Label(self.window, text="A Pagar:").grid(column=0,row=7, sticky="W")        
        ttk.Label(self.window, textvariable=self.total,foreground="orange",borderwidth=5, anchor="e").grid(column=0,row=8)             
                       
        # Botones
        ttk.Button(self.window, text="Calcular", command=self.calcular).grid(column=0,row=6, sticky="WE", padx=10)
        
        self.window.mainloop()
        
    def calcular(self):
        total=0
        hr = int(self.hr.get())
        cr = float(self.ref.get())
        total=hr*cr
        
        if self.aceite.get():
            total+= 100
        if self.rotacion.get():
            total+=200
        if self.anti.get():
            total+=150
        
        

        self.total.set(f"Total: ${total}")
    

if __name__ == '__main__':
    App()
