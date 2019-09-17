from tkinter import *
import math
from pynput.mouse import Listener


canvas_width = 500
canvas_height = 300

cor=[]
master = Tk()
master.title( "FIGURAS" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)

def paint( x,y, button, pressed ):
   
   con=1
   i=0
   j=1
   while (con<=2):
      color = "#000000"
      cor.append(event.x), cor.append( event.y )
      print(cor[i], cor[j])
      w.create_oval( cor[i], cor[j], cor[i]-0.5, cor[j]+0.5, fill = color )
      con += 1
      i=i+2
      j=j+2
      
   print(cor[0],cor[1],cor[2],cor[3])

   


w.bind( "<Button-1>", paint )

message = Label( master, text = "dibuje" )
message.pack( side = BOTTOM )
    

mainloop()

