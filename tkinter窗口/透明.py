import tkinter
import sys
import datetime
now=datetime.datetime.now()
root = tkinter.Tk()
root.overrideredirect(True)
#root.attributes("-alpha", 0.3)窗口透明度70 %
root.attributes("-alpha", 0.5)#窗口透明度60 %
root.geometry("1980x1080")
canvas = tkinter.Canvas(root)
canvas.configure(width = 1980)
canvas.configure(height = 1080)
canvas.configure(bg = "white")
canvas.configure(highlightthickness = 0)
canvas.pack()
var = tkinter.StringVar()
ll=tkinter.Label(root, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var)
var.set(now.year)
#var.set('')
x,y=0,0
def move(event):
    global x,y
    new_x = (event.x-x)+root.winfo_x()
    new_y = (event.y-y)+root.winfo_y()
    s = "1980x1080+" + str(new_x)+"+" + str(new_y)
    root.geometry(s)
canvas.bind("<B1-Motion>",move)
root.mainloop()
