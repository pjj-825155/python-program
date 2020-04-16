import tkinter
import numpy as np

def direction_up(event):
    global coor_x,coor_y,long,width
    if coor_y>0:
        coor_y-=width
    coordibate=f"{long}x{width}+{coor_x}+{coor_y}"
    body.geometry(coordibate)

def direction_down(event):
    global coor_x,coor_y,narrow,long,width
    if coor_y<1080/narrow-width*2:
        coor_y+=width
    coordibate=f"{long}x{width}+{coor_x}+{coor_y}"
    body.geometry(coordibate)

def direction_left(event):
    global coor_x,coor_y,long,width
    if coor_x>0:
        coor_x-=long
    coordibate=f"{long}x{width}+{coor_x}+{coor_y}"
    body.geometry(coordibate)

def direction_right(event):
    global coor_x,coor_y,long,width
    if coor_x<1980/narrow-long*2:
        coor_x+=long
    coordibate=f"{long}x{width}+{coor_x}+{coor_y}"
    body.geometry(coordibate)
    
def direction_key(event):
    global coor_x,coor_y,narrow,long,width
    if event.char=="w":
        if coor_y>0:
            coor_y-=width
    if event.char=="s":
        if coor_y<1080/narrow-width*2:
            coor_y+=width
    if event.char=="a":
        if coor_x>0:
            coor_x-=long
    if event.char=="d":
        if coor_x<1980/narrow-long*2:
            coor_x+=long
    coordibate=f"{long}x{width}+{coor_x}+{coor_y}"
    body.geometry(coordibate)

def set_maze():
    global long,width
    
    

#设置大小
long=90
width=90
#设置位置
coor_x=0
coor_y=0
#设置缩放
narrow=1.25
#设置窗口
body=tkinter.Tk()

#设置迷宫
maze_coor=np.array([["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                    ["#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
                    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                    ["#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
                    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                    ["#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
                    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                    ["#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
                    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]])
maze_x,maze_y=maze_coor.shape
maze_body=[[tkinter.Tk()]*maze_y for i in range(maze_x)]
canvas=[[0]*maze_y for i in range(maze_x)]
#迷宫窗口
for m in range(maze_x):
    for n in range(maze_y):
        maze_body[m][n]=tkinter.Tk()
        maze_body[m][n].overrideredirect(True)
        maze_body[m][n].attributes("-alpha",0.75)
        coordibate=f"{long}x{width}+{maze_x*90}+{maze_y*90}"
        maze_body[m][n].geometry(coordibate)
        canvas[m][n]=tkinter.Canvas(maze_body[m][n])
        canvas[m][n].pack()
        maze_body[m][n].mainloop()

body.overrideredirect(True)
body.attributes("-alpha",0.75)
coordibate=f"{long}x{width}"
body.geometry(coordibate)
canvas = tkinter.Canvas(body)
# 让画布获得焦点,对于键盘
canvas.focus_set()  
canvas.pack()
#监听方向键
canvas.bind("<Up>",direction_up)
canvas.bind("<Down>",direction_down)
canvas.bind("<Left>",direction_left)
canvas.bind("<Right>",direction_right)
canvas.bind("<Key>",direction_key)
body.mainloop()
