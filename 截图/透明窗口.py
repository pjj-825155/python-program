import tkinter
import time
import cv2
import numpy as np
from PIL import ImageGrab
root = tkinter.Tk()
root.overrideredirect(True)
#
file=open("coordinate.txt","w")
#窗口透明度
root.attributes("-alpha", 0.3)
root.geometry("1980x1080")
canvas = tkinter.Canvas(root,width = 1980,height = 1080,bg = "white")
canvas.pack()
count=0
def get_coordinate_left(event):
    global count
    print(event.x,event.y)
    file.write(str(event.x))
    file.write("\n")
    file.write(str(event.y))
    file.write("\n")
    count+=1
    if count==2:
        file.close()
        quit()

def quit_button(event):
    quit()


canvas.bind("<Button-3>",quit_button)
canvas.bind("<Button-1>",get_coordinate_left)
canvas.mainloop()
