import tkinter as tk
#定义函数，用于实现改变标签的内容
def btnHelloClicked():
    labelHello.config(text='Hello tkinter')
top = tk.Tk()
top.geometry('200x200')
top.title('Button Text')
labelHello = tk.Label(top, text = '按下按钮', height = 5, width = 20,fg = 'blue')
labelHello.pack()
btn = tk.Button(top, text='hello', command=btnHelloClicked)
btn.pack()
top.mainloop()
