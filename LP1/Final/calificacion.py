import tkinter as tk
from tkinter import ttk

class App():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ulsa Chihuahua")


        #Titulo
        ttk.Label(self.window, text="Física", font=("Arial, 15"),foreground="Black").grid(row=0, column=1, padx=50, columnspan=8, sticky="W")
        #3 parciales
        ttk.Label(self.window, text="3 Parciales (40%)", font=("Arial, 9")).grid(row=1, column=0, padx=20, columnspan=5, sticky="W")

        #Entry
        self.p1 = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.p1).grid(row=2, column=0, padx=20)
        #Entry
        self.p2 = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.p2).grid(row=2, column=1, padx=20)
        #Entry
        self.p3 = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.p3).grid(row=2, column=2, padx=20)
        
        #Examen final
        ttk.Label(self.window, text="Examen Final (30%)", font=("Arial, 9")).grid(row=3, column=0, padx=20, columnspan=5, sticky="W")
        #Entry
        self.ef = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.ef).grid(row=4, column=0, padx=20)
        
        #Examen final
        ttk.Label(self.window, text="Trabajo Final (20%)", font=("Arial, 9")).grid(row=5, column=0, padx=20, columnspan=5, sticky="W")
        #Entry
        self.tf = tk.DoubleVar()
        ttk.Entry(self.window, textvariable=self.tf).grid(row=6, column=0, padx=20)
        
        # Checkbutton (Participacion)
        self.par = tk.BooleanVar()        
        ttk.Checkbutton(self.window, text='Participación (10%)',variable=self.par,onvalue=True, offvalue=False).grid(column=0,row=7,padx=20, sticky="W")
        
        #Boton
        ttk.Button(self.window, text="Calcular", command=self.calcular).grid(row=8, column=1)
        
        #Resultado
        self.resultado = tk.StringVar()
        self.resultado.set("CALIFICACIÓN FINAL: ")
        ttk.Label(self.window, textvariable=self.resultado, font=("Arial, 12")).grid(row=5, column=1, padx=20, pady=10)
        
        #Foto
        self.photo = tk.PhotoImage()
        ttk.Label(self.window,image= self.photo).grid(column=2,row=6,rowspan=3)  


        self.window.mainloop()

    def calcular(self):
        p1 =self.p1.get()
        p2=self.p2.get()
        p3=self.p3.get()
        final=self.ef.get()
        traf=self.tf.get()
        pr=((p1+p2+p3)/3)*.40
        ef=final*.30
        tf=traf*.20
        
        total=pr+ef+tf
        
        if self.par.get():
            total=total*1.10
        
        
        if total<70:
            self.photo.configure(file="./img/mal2.png")
            
        elif total>69:
            self.photo.configure(file="./img/bien2.png")
            

        self.resultado.set(f"Resultado: {round(total, 2)}")
        
if __name__ == '__main__':
    App()