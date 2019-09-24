import math
import random
from tkinter import *
xx=[]
yy=[]

def posicion(event):
    xx.append(event.x)
    yy.append(event.y)
    ventana.create_oval((event.x)-1,(event.y)-1,(event.x)+1,(event.y)+1, fill="black")

def dibujar():
    opcion = var.get()
    xx.append(xx[0]-xx[1])
    yy.append(yy[0]-yy[1])
    diagonal=(math.sqrt((pow(xx[2],2))+(pow(yy[2],2))))  
    print (xx)
    print (yy)
    print (diagonal)
    
    if opcion==1:
        radio=diagonal/2
        ventana.create_oval(xx[0],yy[0],xx[1], yy[1],fill="green")
        result1.set("Perimetro:"+str(2*math.pi*radio))
        result2.set("Area:"+str(math.pi*(pow(radio,2))))
        print (radio)
    if opcion==2:
        ventana.create_rectangle(xx[1], yy[0],xx[0], yy[0],fill="blue",width=0)
        ventana.create_line(xx[1], yy[0],xx[0], yy[0],fill="red")
        ventana.create_line(xx[1], yy[0],xx[1], yy[1],fill="red")
        ventana.create_line(xx[0], yy[1],xx[0], yy[0],fill="blue")
        ventana.create_line(xx[0], yy[1],xx[1], yy[1],fill="blue")
        result1.set("Perimetro:"+str((abs(xx[0]-xx[1])*2)+(abs(yy[0]-yy[1])*2)))
        result2.set("Area:"+str((xx[0]-xx[1])*(yy[0]-yy[1])))
        print (abs(xx[0]-xx[1]))
        print (abs(yy[0]-yy[1]))
    if opcion==3:
        ventana.create_line(xx[0], yy[0],xx[1], yy[1],fill="white")
        ventana.create_line(xx[0], yy[1],xx[1], yy[1],fill="white")
        ventana.create_line(xx[0], yy[1],xx[0], yy[0],fill="white")
        result1.set("Perimetro:"+str(abs(xx[0]-xx[1])+abs(yy[0]-yy[1])+diagonal))
        result2.set("Area:"+str(((xx[0]-xx[1])*(yy[0]-yy[1]))/2))
        print (abs(xx[0]-xx[1]))
        print (abs(yy[0]-yy[1]))
        print (diagonal)
            
root=Tk()
root.title("Figuras")
root.geometry("400x500")
root.configure(background="white")
var= IntVar()
ventana=Canvas(root,width=400,height=400,background="grey")
ventana.pack()
ventana.place(x=0,y=100)
ventana.bind("<Button-1>", posicion)

btc = Button(root,text="Circulo" ,variable=var ,value=1)
btc.grid(row=1, column=0, sticky=W)
btr = Button(root,text="Rectangulo" ,variable=var ,value=2)
btr.grid(row=2, column=0, sticky=W)
btt = Button(root,text="Triangulo" ,variable=var ,value=3)
btt.grid(row=3, column=0, sticky=W)

result1= StringVar()
result2= StringVar()

etiqueta1=Label(root, textvariable = result1)
etiqueta1.grid(row=1, column=5)

etiqueta2=Label(root, textvariable = result2)
etiqueta2.grid(row=2, column=5)



marco.mainloop()
    
