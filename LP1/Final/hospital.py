import tkinter as tk
from tkinter import ttk

class App():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hospital Chihuahua")


        #Titulo
        ttk.Label(self.window, text="Paciente", font=("Arial, 15"),foreground="Black").grid(row=0, column=0, padx=25, sticky="W")
        
        #Radio buttons
        self.tipo = tk.StringVar()
        ttk.Label(self.window, text="   Tipo de enfermedad:", font=("Arial, 12")).grid(column=0,row=1, sticky="W")
        ttk.Radiobutton(self.window, text='Respiratorio', variable=self.tipo, value='r').grid(column=0,row=2, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text='Digestivo', variable=self.tipo, value="d").grid(column=0,row=3, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text='Fractura', variable=self.tipo, value='f').grid(column=0,row=4, sticky="W", padx=20)

        
        
        #Edad
        ttk.Label(self.window, text="Edad", font=("Arial, 10")).grid(row=5, column=0, padx=20, columnspan=5, sticky="W")
        #Entry
        self.ed = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.ed).grid(row=6, column=0, padx=20)
        
        #Dias Hosp
        ttk.Label(self.window, text="Días Hospitalizado", font=("Arial, 10")).grid(row=7, column=0, padx=20, columnspan=5, sticky="W")
        #Entry
        self.dh = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.dh).grid(row=8, column=0, padx=20)
        
        #Boton
        ttk.Button(self.window, text="Calcular", command=self.calcular).grid(row=8, column=1)
        
        #Resultado
        self.resultado = tk.StringVar()
        self.resultado.set("A pagar: ")
        ttk.Label(self.window, textvariable=self.resultado, font=("Arial, 12")).grid(row=5, column=1, padx=20, pady=10)
        
        #IMAGEN
        self.photo2 = tk.PhotoImage (file = "./img/captura.png")
        ttk.Label (self.window, image = self.photo2).grid (column = 1, row = 3)
        


        self.window.mainloop()

    def calcular(self):
        ed= self.ed.get()
        dias=self.dh.get()
        tipo = self.tipo.get()
        total=0
        
        if tipo == "r":
            total= total+80
        if tipo == "d":
            total = total+115
        if tipo == "f":
            total = total+145
        total=total
            
        if ed>=14 and ed<=22:
            total=(total*dias)*1.10
        else:
            total=total*dias
     
    
        self.resultado.set(f"A pagar: ${round(total, 2)}")
        
if __name__ == '__main__':
    App()