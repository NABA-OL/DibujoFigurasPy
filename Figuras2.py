import math
import random
import tkinter as tk
from tkinter import *
xx=[]
yy=[]

def posicion(event):
    xx.append(event.x)
    yy.append(event.y)
    lienzo.create_oval((event.x)-2,(event.y)-2,(event.x)+2,(event.y)+2, fill="black")

def dibujar():
    opcion = var.get()
    xx.append(xx[0]-xx[1])
    yy.append(yy[0]-yy[1])
    diagonal=(math.sqrt((pow(xx[2],2))+(pow(yy[2],2))))  
    
    if opcion==1:
        radio=diagonal/2
        lienzo.create_oval(xx[0],yy[0],xx[1], yy[1],fill="skyblue")
        result1.set("Perimetro:"+str(2*math.pi*radio))
        result2.set("Area:"+str(math.pi*(pow(radio,2))))
    if opcion==2:
        lienzo.create_line(xx[1], yy[0],xx[0], yy[0],fill="red")
        lienzo.create_line(xx[1], yy[0],xx[1], yy[1],fill="red")
        lienzo.create_line(xx[0], yy[1],xx[0], yy[0],fill="blue")
        lienzo.create_line(xx[0], yy[1],xx[1], yy[1],fill="blue")
        result1.set("Perimetro:"+str((abs(xx[0]-xx[1])*2)+(abs(yy[0]-yy[1])*2)))
        result2.set("Area:"+str((xx[0]-xx[1])*(yy[0]-yy[1])))
        
    if opcion==3:
        lienzo.create_line(xx[0], yy[0],xx[1], yy[1],fill="white")
        lienzo.create_line(xx[0], yy[1],xx[1], yy[1],fill="white")
        lienzo.create_line(xx[0], yy[1],xx[0], yy[0],fill="white")
        result1.set("Perimetro:"+str(abs(xx[0]-xx[1])+abs(yy[0]-yy[1])+diagonal))
        result2.set("Area:"+str(((xx[0]-xx[1])*(yy[0]-yy[1]))/2))
    
marco=tk.Tk()
marco.title("Dibujo figuras")
marco.geometry("400x430")
marco.configure(background="white")
var= tk.IntVar()
lienzo=Canvas(marco,width=400,height=400,background="grey")
lienzo.pack()
lienzo.place(x=0,y=30)
lienzo.bind("<Button-1>", posicion)

b1 = tk.Radiobutton(marco,text ='Circulo' ,variable=var ,value=1)
b1.grid(row=0, column=1, sticky=tk.W)
b2 = tk.Radiobutton(marco,text ='Cuadrado' ,variable=var ,value=2)
b2.grid(row=0, column=2, sticky=tk.W)
b3 = tk.Radiobutton(marco,text ='Triangulo' ,variable=var ,value=3)
b3.grid(row=0, column=3, sticky=tk.W)

result1= tk.StringVar()
result2= tk.StringVar()

etiqueta1=tk.Label(marco, textvariable = result1)
etiqueta1.grid(row=1, column=4)

etiqueta2=tk.Label(marco, textvariable = result2)
etiqueta2.grid(row=2, column=4)


tk.Button(marco,text='Dibujar',command=dibujar).grid(row=0,column=0,sticky=tk.W,pady=4)

marco.mainloop()
    
