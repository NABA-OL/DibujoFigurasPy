from tkinter import *
import math


canvas_width = 500
canvas_height = 300

def paint( event ):
   cor=[]
   con=1
   i=0
   j=1
   while (con<=2):
      color = "#000000"
      print("clicked at: ", event.x, event.y)
      cor.append(event.x)
      cor.append( event.y )
      w.create_oval( cor[i], cor[j], cor[i]-0.5, cor[j]+0.5, fill = color )
      con += 1
      i=i+2
      j=j+2
      
   print(cor[0],cor[1],cor[2],cor[3])

   

master = Tk()
master.title( "FIGURAS" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<Button-1>", paint )

message = Label( master, text = "dibuje" )
message.pack( side = BOTTOM )
    

window.mainloop()

