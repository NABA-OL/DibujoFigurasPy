import math
from tkinter import*
import tkinter as tk
"""NABA-OL"""

        
class Figura:
    global coordenadas
    global coordenadasy
    global coordenadasx
    def posicion(event):
        coordenadasx.append(event.x)
        coordenadasy.append(event.y)
        ventana.create_oval(event.x-1,event.y-1,event.x+1,event.y+1,fill="black",outline="white", width=0)

    def calcArea(resultarea):
        self.resultarea
    
    def calcPerimetro(resultperimetro):
        self.resultarea
              
class Circulo (Figura):
    global coordenadas
    global coordenadasy
    global coordenadasx
    def distancia():
        coordenadasx.append(xx[0]-xx[1])
        coordenadasy.append(yy[0]-yy[1])
        diagonal=(math.sqrt((pow(coordenadasx[2],2))+(pow(coordenadasy[2],2))))
        radio=diagonal/2
    def calcArea(resultarea):
        resultarea.set("Area:"+str(math.pi*(pow(distancia.radio,2))))
        return resultarea
    
    def calcPerimetro(resultperimetro):
        resultperimetro.set("Perimetro:"+str(2*math.pi*distancia.radio))
        return resultperimetro

    def circulo():
        
        ventana.create_oval(coordenadasx[0],coordenadasy[0],coordenadasx[1], coordenadasy[1],fill="skyblue")
    
class Rectangulo(Figura):
    global coordenadas
    global coordenadasy
    global coordenadasx
    
    def calcArea (resultarea):
        resultarea.set("Area:"+str((coordenadax[0]-coordenadax[1])*(coordenadasy[0]-coordenadasy[1])))
        return resultarea
    def calcPerimetro(resultperimetro):
        resultperimetro.set("Perimetro:"+str((abs(coordenadax[0]-coordenadax[1])*2)+(abs(coordenadasy[0]-coordenadasy[1])*2)))
        return resultperimetro
    
    def rectangulo():
       
        ventana.create_rectangle(coordenadasx[1], coordenadasy[0],coordenadasx[0], coordenadasy[1],fill="black")
            
class Triangulo (Figura):
    global coordenadas
    global coordenadasy
    global coordenadasx
    
    def calcArea (self):
        resultarea.set("Area:"+str(((coordenadasx[0]-coordenadasx[1])*(coordenadasy[0]-coordenadasy[1]))/2))
        return resultarea
    
    def calcPerimetro(self):
        diagonal=(math.sqrt((pow(coordenadasx[2],2))+(pow(coordenadasy[2],2))))
        resultperimetro.set("Perimetro:"+str(abs(coordenadasx[0]-coordenadasx[1])+abs(coordenadasy[0]-coordenadasy[1])+diagonal))
        return resultperimetro

    def triangulo():
        ventana.create_line(coordenadasx[0], coordenadasy[0],coordenadasx[1], coordenadasy[1],fill="white")
        ventana.create_line(coordenadasx[0], coordenadasy[1],coordenadasx[1], coordenadasy[1],fill="white")
        ventana.create_line(coordenadasx[0], coordenadasy[1],coordenadasx[0], coordenadasy[0],fill="white")
        


root = Tk()
root.geometry("400x480")
root.title("Figuras")
coordenadas  = []
coordenadasx=[]
coordenadasy=[]
ventana = Canvas(root,width=400,height=400,background="grey")
ventana.pack()
ventana.place(x=0,y=0)
ventana.bind("<Button-1>", Figura.posicion)
resultarea= tk.StringVar()
resultperimetro= tk.StringVar()

btc = Button(root,text="Circulo",command=Circulo.circulo)

btr = Button(root,text="Rectangulo",command=Rectangulo.rectangulo)
btt = Button(root,text="Triangulo",command=Triangulo.triangulo)
btA=Button(root,text="Area",command=Figura.calcArea)
btA.pack()
btA.place(x=200,y=403)

btt.pack()
btt.place(x=122,y=403)
btc.pack()
btc.place(x=0,y=403)
btr.pack()
btr.place(x=50,y=403)

etiqueta1=tk.Label(root, text = "HOLIS AQUI VA EL AREA", textvariable = "HOLIS AQUI VA EL AREA")
etiqueta1.place(x=0, y=430)
etiqueta2=tk.Label(root, text = "HOLIS AQUI VA EL Perimetro" , textvariable = "HOLIS AQUI VA EL peri")
etiqueta2.place(x=0, y=450)

root.mainloop()
        

    
