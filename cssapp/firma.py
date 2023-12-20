import sys
from tkinter import *
from PIL import Image, ImageDraw
drawing_area=""
x, y=None, None
count=0
image_cont=0
image_name="firma"
pil_image=Image.new("1",(200,200),"white")
draw=ImageDraw.Draw(pil_image)

def quitar(event):
    sys.exit()

def limpiar(event):

    global drawing_area,pil_image,draw
    drawing_area.delete("all")
    pil_image=Image.new("1",(200,200),"white")
    draw=ImageDraw.Draw(pil_mage)

def firmar(event):
    global drawing_area, x, y, count, draw
    newx, newy=event.x, event.y
    if x is None:
        x, y=newx, newy
        return
    count+=1
    sys.stdout.write("revent count%d" % count)
    drawing_area.create_line((x, y, newx, newy),width=5,smooth=True)
    draw.line((x,y,newx,newy),width=10)
    x, y=newx, newy

def firmado(event):
    global x,y
    x, y=None, None

def guardar(event):
    global pil_image, image_name,image_cont
    image_cont+=1
    file_name=image_name+str(image_cont)+".jpg"
    pil_image=pil_image.resize((300,300),Image.Resampling.LANCZOS)
    pil_image.save(file_name)

def main():
    global drawing_area
    win=Tk()
    win.title("LIENZO PARA DIBUJAR")
    drawing_area=Canvas(win,width=500, height=500, bg="white" )
    drawing_area.bind("<B1-Motion>", firmar)
    drawing_area.bind("<ButtonRelease>", firmado)
    drawing_area.pack()

    b1=Button(win, text="SALIR", bg="red")
    b1.pack()
    b1.bind("<Button-1>", quitar)
    b2=Button(win, text="LIMPIAR", bg="blue")
    b2.pack()
    b2.bind("<Button-1>", limpiar)
    b3=Button(win, text="GUARDAR", bg="green")
    b3.pack()
    b2.bind("<Button-1>", guardar)
    win.mainloop()
if __name__=="__main__":
    main()





