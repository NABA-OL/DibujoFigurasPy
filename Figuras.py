import math
from tkinter import*
"""NABA-OL"""

        
class Figura:
    global coordenadas
    def posicion(event):
        coordenadas.append(str(event.x)+","+str(event.y))
        ventana.create_oval(event.x-1,event.y-1,event.x+1,event.y+1,fill="black",outline="white", width=0)
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x=int(coordenadas[0])
        self.p2x=int(coordenadas[1])
        self.p1y=int(coordenadas[2])
        self.p2y=int(coordenadas[3])

    def distancia(self, p1x, p1y, p2x=0, p2y=0):
        math.sqrt((p1x-p2x)**2+(p1y-p2y)**2)
        return distancia

    def linea():
        
        s = -1
        for pos in coordenadas:
            xy = pos.split(",")
            x = xy[0]
            y =  xy[1]
            if s== -1:
                s = 1
                antx = x
                anty = y
            else:
                ventana.create_line(antx,anty,x,y,smooth=TRUE,fill="black")
                antx = x
                anty = y

              

class Circulo (Figura):
    global coordenadas
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x=p1x
        self.p2x=p2x
        self.p1y=p1y
        self.p2y=p2y    
    
    def calcArea(self):
        self.dist = self.distancia(self.p1x, self.p1y, self.p2x, self.p2y)
        self.area = math.pi * (self.dist**2)
        return self.area
    
    def calcPerimetro(self):
        self.dist = self.distancia(self.p1x, self.p1y, self.p2x, self.p2y)
        self.perimetro = 2 * math.pi * self.dist
        return self.perimetro

    def circulo():
        
        s = -1
        for pos in coordenadas:
            xy = pos.split(",")
            x = xy[0]
            y =  xy[1]
            if s== -1:
                s = 1
                antx = x
                anty = y
            else:
                ventana.create_oval(int(x),int(y),int(antx),int(anty),fill="skyblue",outline="white",width=0)
                antx = x*2
                anty = y*2
    
class Rectangulo(Figura):
    global coordenadas
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x=p1x
        self.p2x=p2x
        self.p1y=p1y
        self.p2y=p2y
    
    def calcArea1 (self):
        self.base = self.p2x-self.p1x
        self.altura = self.p2y-self.p1y  
        self.area=self.base*self.altura
        return self.area
    
    def calcArea (self):
        return self.calcArea1()
    
    def calcPerimetro(self):
        return (2*self.distancia(self.p1x, self.p2x))+(2*self.distancia(self.p1y, self.p2y))

    def rectangulo():
       
        s = -1
        for pos in coordenadas:
            xy = pos.split(",")
            x = xy[0]
            y =  xy[1]
            if s== -1:
                s = 1
                antx = x
                anty = y
            else:
                ventana.create_rectangle(antx,anty,x,y,fill="blue",width=0)
                antx = x
                anty = y
    
class Triangulo (Rectangulo):
    global coordenadas
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x=p1x
        self.p2x=p2x
        self.p1y=p1y
        self.p2y=p2y
    
    def calcArea (self):
        return self.calcArea1()/2
    
    def calcPerimetro(self):
        return self.distancia(self.p1x, self.p2x)+self.distancia(self.p1y, self.p2y)+self.distancia(self.p1x, self.p1y, self.p2x, self.p2y)

    def dtriangulo():
        
        s = -1
        for pos in coordenadas:
            xy = pos.split(",")
            x = xy[0]
            y =  xy[1]
            if s== -1:
                s = 1
                antx = x
                anty = y
            else:
                ventana.create_polygon(antx,anty,x,y,int(x)-int(anty),int(y)+int(antx),fill='yellow',outline='white', width=0)
                antx = x
                anty = y

root = Tk()
root.geometry("400x430")
root.title("Figuras")
coordenadas  = []
ventana = Canvas(root,width=400,height=400,background="grey")
ventana.pack()
ventana.place(x=0,y=0)
ventana.bind("<Button-1>", Figura.posicion)

btl = Button(root,text="Linea",command=Figura.linea)
btc = Button(root,text="Circulo",command=Circulo.circulo)
btr = Button(root,text="Rectangulo",command=Rectangulo.rectangulo)
btt = Button(root,text="Triangulo",command=Triangulo.dtriangulo)

btt.pack()
btt.place(x=172,y=403)
btl.pack()
btl.place(x=10,y=403)
btc.pack()
btc.place(x=50,y=403)
btr.pack()
btr.place(x=100,y=403)

root.mainloop()
        

    
