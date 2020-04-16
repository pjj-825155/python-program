import tkinter as tk
num=0
window = tk.Tk()
window.geometry('500x300')
window.attributes("-alpha", 0.5)
var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='white', fg='black', font=('Arial', 12), width=30, height=2)
l.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('%d'%num)
    else:
        on_hit = False
        var.set('暂停')
b = tk.Button(window, text='start', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()
num+=1
window.mainloop()
