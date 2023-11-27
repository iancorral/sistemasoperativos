import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st

class App():
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rango Metros")
        self.window.geometry("600x600")

        #Texto
        ttk.Label(self.window, text="Rango Metros", font=("Arial", 16)).grid(column=0, row=0, padx=10, pady=10, columnspan=3)

        #Texto
        ttk.Label(self.window, text="De", font=("Arial", 10)).grid(column=0, row=1)
        ttk.Label(self.window, text="Hasta", font=("Arial", 10)).grid(column=1, row=1)

        #Entry
        self.v1 = tk.IntVar()
        ttk.Entry(self.window, textvariable=self.v1).grid(column=0, row=2, padx=5, pady=5)

        self.v2 = tk.IntVar()
        ttk.Entry(self.window, textvariable=self.v2).grid(column=1, row=2, padx=5, pady=5)

        #Boton
        ttk.Button(self.window, text=("Mostrar"), command=self.calcular).grid(column=2, row=2, padx=5, pady=5)

        #Scrolltext
        self.scrollt = st.ScrolledText(self.window, width = 40, height = 8, font = ("Courier",15))
        self.scrollt.grid(column = 0, row=3, columnspan=3, padx=10, pady=10)

        #Inicio del programa
        self.window.mainloop()

    def calcular(self):
        self.scrollt.delete("1.0",tk.END)
        self.scrollt.insert(tk.INSERT, f"Metros\tYardas\tPies\tPulgadas\n")

        for i in range(self.v1.get(), self.v2.get()+1):
            self.scrollt.insert(tk.INSERT, f"{i}\t{round(i*1.09,2)}\t{round(i*3.28,2)}\t{round(i*39.37,2)}\n")
        

if __name__ == '__main__':
    App()