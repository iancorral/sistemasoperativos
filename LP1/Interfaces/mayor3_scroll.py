import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st
import random

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Mayor')

        ttk.Label(self.window, text="Mayor de 3 números", font=("Arial",20),
            foreground="blue").grid(column=0, row=0, columnspan=2)
        self.scrollt = st.ScrolledText(self.window, width = 30, height = 8,font = ("Courier",15))
        self.scrollt.grid(column = 0, row=1, pady = 10, padx = 10)
        ttk.Button(self.window, text="Mostrar",command=self.mostrar).grid(column=0, row=2)

        self.window.mainloop()
        
    def mostrar(self):
        self.scrollt.delete("1.0",tk.END)
        self.scrollt.insert(tk.INSERT, f"#1\t#2\t#3\tMayor\n")
        for i in range(10):
            n1 = random.randint(0,100)
            n2 = random.randint(0,100)
            n3 = random.randint(0,100)
            if n1>n2 and n1>n3:
                mayor = n1
            elif n2 > n3:
                mayor = n2
            else:
                mayor = n3
            self.scrollt.insert(tk.INSERT, f"{n1}\t{n2}\t{n3}\t{mayor}\n")

if __name__ == '__main__':
    App()