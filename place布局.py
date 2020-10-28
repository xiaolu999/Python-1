from tkinter import *
root =Tk()
root.geometry('300x200')
la = Label(root, text = 'hello place a')  #创建标签la

la.place(x = 0, y = 0, anchor = NW)           #使用绝对坐标将Labeel放在（0,0）上
lb = Label(root, text = 'hello place b')
lb.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()