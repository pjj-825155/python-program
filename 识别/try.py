import tkinter
root = tkinter.Tk()
root.overrideredirect(True)
#
file=open("coordinate.txt","w")
#窗口透明度
root.attributes("-alpha", 0.25)
root.geometry("1980x1080")
canvas = tkinter.Canvas(root,width = 1980,height = 1080,bg = "white")
canvas.pack()
click_x,click_y=0,0

def quit_button(event):
    quit()

def left_slide(event):
    global click_x,click_y
    canvas.delete("rectangle")
    canvas.create_rectangle(click_x,click_y,event.x,event.y,fill="white",tags="rectangle")
    canvas.pack()
    

def left_click(event):
    global click_x,click_y
    click_x,click_y=event.x,event.y
    file.write(str(event.x))
    file.write("\n")
    file.write(str(event.y))
    file.write("\n")

def left_release(event):
    file.write(str(event.x))
    file.write("\n")
    file.write(str(event.y))
    file.write("\n")
    file.close()
    quit()

canvas.bind("<Button-3>",quit_button)
canvas.bind("<Button-1>",left_click)
canvas.bind("<B1-Motion>",left_slide)
canvas.bind("<ButtonRelease-1>",left_release)
root.mainloop()
