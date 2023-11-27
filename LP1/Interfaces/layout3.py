import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Layout #2")
        self.window.geometry("350x400")
    
        ttk.Label(self.window,text="ULSA",font="Arial, 30").grid(column=1,row=0,pady=20)
        ttk.Button(self.window, text="Enviar").grid(column=0,row=1,pady=10,padx=10)
        ttk.Button(self.window, text="Cancelar").grid(column=1,row=1,pady=10,padx=10)
        ttk.Button(self.window, text="Ayuda").grid(column=2,row=1,pady=10,padx=10)
        
        photo=tk.PhotoImage(file="./img/carro2.png")
        ttk.Label(self.window,image=photo).grid(column=0,row=2,pady=10,padx=10,columnspan=10,ipadx=20)
        
        self.window.mainloop()




if __name__=='__main__':
    app= App()
