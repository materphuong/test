import PIL
from PIL import ImageTk, Image, ImageDraw
from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import cv2

width = 200
height = 200
white =(255 , 255 , 255)
black =(0 , 0 , 0)

def Run():
    img = cv2.imread('digits.png',0)
    imgNhanDang = cv2.imread('image_20.png',0)

    cells = [np.hsplit(row , 100) for row in np.vsplit(img, 50)]

    X= np.array(cells)
    x2= np.array(imgNhanDang)

    train = X[:,:50].reshape(-1,400).astype(np.float32)
    test = x2.reshape(-1, 400).astype(np.float32)

    k =np.arange(10)
    train_labels = np.repeat(k, 250)[:, np.newaxis]

    knn = cv2.ml.KNearest_create()
    knn.train(train, 0 , train_labels)
    kq1, kq2, kq3, kq4 =knn.findNearest(test, 20)

    box.insert(END,"Kết quả là: {}".format(int(kq2)))

def CLEAR():
    box.delete(1.0,END)
    global image1, draw;

    cv.delete("all")
    image1 = PIL.Image.new("RGB" ,(width, height),black)
    draw = ImageDraw.Draw(image1)

def SAVE():
    filename = "image.png"
    image1.save(filename)
    image = Image.open('image.png')
    new_image =image.resize((20, 20))
    new_image.save('image_20.png')

def paint(event):
    x1, y1 =(event.x - 3), (event.y - 3)
    x2, y2 =(event.x + 3), (event.y + 3)
    cv.create_line(x1, y1 , x2 , y2, fill="white",width=15)
    draw.line([x1,y1,x2,y2],fill="white",width=15)
    
root = Tk()
root.geometry("1280x721+90+30")
root.title("Nhóm 2")
background=Image.open("giaodien.png")
render=ImageTk.PhotoImage(background)
img3=Label(root ,image=render)
img3.place(x=0,y=0)

cv =Canvas(root, width=width,height=height,bg='black')
cv.place(x=185, y=280)

image1 =PIL.Image.new("RGB", (width,height),black)
draw = ImageDraw.Draw(image1)

cv.bind("<B1-Motion>", paint)

button_frame=Frame(root).pack(side=BOTTOM)
save_button=Button(button_frame,text="SAVE",font=(("Times New Romen"),15,'bold'),command=SAVE)

save_button.place(x=250,y= 500)

box=Text(root,width=25, height=1,font=("Times New Romen",13))
box.pack(pady=300)

button_frame=Frame(root).pack(side=BOTTOM)
run_button=Button(button_frame,text="RUN",font=(("Times New Romen"),15,'bold'),command=Run)
run_button.place(x=545, y=325)

button_frame =Frame(root).pack(side=BOTTOM)
clear_button=Button(button_frame,text="CLEAR",font=(("Times New Romen"),15,'bold'),command=CLEAR)
clear_button.place(x=650, y=325)
root.mainloop()

