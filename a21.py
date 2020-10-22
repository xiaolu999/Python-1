import tkinter


windows = tkinter.Tk()
windows.title('金企鹅')
c = tkinter.Label(windows,text = '你好呀',fg = 'blue',bg = 'red',font = ('宋体'),width = 20,height = 4)
c.pack()
windows.geometry('400x500')

windows.mainloop()