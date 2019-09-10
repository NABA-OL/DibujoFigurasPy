from tkinter import *

canvas_width = 500
canvas_height = 300

def paint( event ):
   color = "#000000"
   print("clicked at: ", event.x, event.y)
   x1, y1 = ( event.x - 0.5), ( event.y -0.55 )
   x2, y2 = ( event.x + 0.5 ), ( event.y + 0.5 )
   w.create_oval( x1, y1, x2, y2, fill = color )

master = Tk()
master.title( "hijueperra" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<Button-1>", paint )

message = Label( master, text = "dibuje" )
message.pack( side = BOTTOM )
    
mainloop()


