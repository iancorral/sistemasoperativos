import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Ulsa")
        
        #numero 1
        self.n1=tk.IntVar()
        ttk.Label (self.window,text="Numero 1: ").grid(column=0,row=0)
        ttk.Entry(self.window, textvariable=self.n1).grid(column=1,row=0)
        
        #numero 2
        self.n2=tk.IntVar()
        ttk.Label (self.window,text="Numero 2: ").grid(column=0,row=1)
        ttk.Entry(self.window,textvariable=self.n2).grid(column=1,row=1)
        
        #boton
        ttk.Button(self.window,text="Calcular",command=self.calcular).grid(column=0,row=2,columnspan=2,sticky="we")
        
        #img
        photo=tk.PhotoImage(file="./img/carro2.png")
        ttk.Label(self.window,image=photo).grid(column=2,row=0,rowspan=3)
        
        #Resultado
        self.r=tk.StringVar()
        ttk.Label(self.window, textvariable=self.r).grid(column=1,row=3)
        
        self.window.mainloop()
        
    def calcular(self):
        messagebox.showinfo(title="SUMA",message="Hola")
        n1=self.n1.get()
        n2=self.n2.get()
        suma=n1+n2 
        self.r.set(f"Suma={suma}")   
        

if __name__=="__main__":
    app=App()