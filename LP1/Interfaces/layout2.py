import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Ulsa")
        self.window.geometry("300x200")
    
        ttk.Label(self.window,text="Teclado").grid(column=1,row=0,pady=20)
        ttk.Button(self.window, text="A").grid(column=0,row=1,pady=10,padx=10)
        ttk.Button(self.window, text="B").grid(column=1,row=1,pady=10,padx=10)
        ttk.Button(self.window, text="C").grid(column=2,row=1,pady=10,padx=10)
        ttk.Button(self.window, text="D").grid(column=0,row=2,pady=10,padx=10)
        ttk.Button(self.window, text="E").grid(column=1,row=2,pady=10,padx=10)
        ttk.Button(self.window, text="F").grid(column=2,row=2,pady=10,padx=10)
        ttk.Button(self.window, text="G").grid(column=0,row=3,pady=10,padx=10)
        ttk.Button(self.window, text="H").grid(column=1,row=3,pady=10,padx=10)
        ttk.Button(self.window, text="I").grid(column=2,row=3,pady=10,padx=10)
        
        self.window.mainloop()




if __name__=='__main__':
    app= App()