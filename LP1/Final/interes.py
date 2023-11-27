import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st

class App():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora")


        #Inversion inicial
        ttk.Label(self.window, text="Inversion inicial:", font=("Arial, 12")).grid(row=0, column=0, padx=25, sticky="W")
        
        #resultado
        ttk.Label(self.window, text="Resultado inversion por mes:", font=("Arial, 12")).grid(row=0, column=1, padx=25, sticky="W")
        #Entry
        self.invi = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.invi).grid(row=1, column=0, padx=20)
        
        #Radio buttons
        self.meses = tk.StringVar()
        ttk.Label(self.window, text="   Meses:", font=("Arial, 12")).grid(column=0,row=2, sticky="W")
        ttk.Radiobutton(self.window, text='6', variable=self.meses, value='6').grid(column=0,row=3, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text="12", variable=self.meses, value="12").grid(column=0,row=4, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text='18', variable=self.meses, value='18').grid(column=0,row=5, sticky="W", padx=20)
        
        #Interes mensual
        ttk.Label(self.window, text="Interes mensual: ", font=("Arial, 10")).grid(row=6, column=0, padx=20, columnspan=5, sticky="W")
        #Entry
        self.im = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.im).grid(row=7, column=0, padx=20)
        
        # Checkbutton (Mostrar en dolares)
        self.dolares = tk.BooleanVar()        
        ttk.Checkbutton(self.window, text='Mostrar en dolares',variable=self.dolares,onvalue=True, offvalue=False).grid(column=0,row=8,padx=20, sticky="W")
        
        #Boton
        ttk.Button(self.window, text="Calcular", command=self.calcular).grid(row=8, column=1)
        
        #Scroll
        self.scrollt =st.ScrolledText(self.window, width = 40, height = 8, font = ("Courier",15))
        self.scrollt.grid(column = 1, row=1, columnspan=3, padx=10, pady=10)



        self.window.mainloop()

    def calcular(self):
       invi=self.invi.get()
       im=self.im.get()/100
       meses=self.meses.get()
       total=invi*(1+im)
       self.scrollt.delete("1.0",tk.END)
       self.scrollt.insert(tk.INSERT, f"#Mes\t#Pesos\t#Dolares\n")
       
       if self.dolares.get():
            dolares = (total) / 20
       else:
            dolares = 0
        
       if meses == "6":
            for i in range(1,7):
                self.scrollt.insert(tk.INSERT, f"{i}\t{round(i*total)}\t{round(i * dolares)}\n")
                i +=1
       elif meses == "12":
            for i in range(1,13):
                self.scrollt.insert(tk.INSERT, f"{i}\t{round(i*total)}\t{round(i * dolares)}\n")
                i+=1
       elif meses == "18":
            for i in range(1,19):
                self.scrollt.insert(tk.INSERT, f"{i}\t{round(i*total)}\t {round(i * dolares)}\n")
                i +=1
if __name__ == '__main__':
    App()