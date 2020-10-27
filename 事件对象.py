import tkinter
window = tkinter.Tk()
window.title('标题')
window.geometry('200x200')

#鼠标单击绑定事件

def func(event):
    print('单击')
window.bind('<Button-1>', func)
#鼠标双击绑定事件

def func1(event):
    print('双击')
window.bind('<Double-Button-1>', func1)
#鼠标移入绑定事件

def func2(event):
    print('鼠标移入')
window.bind('<Enter>', func2)

#实现拖拽功能
def func3(event):
    x = str(event.x_root)
    y = str(event.y_root)
    window.geometry('200x100+'+x+'+'+y)
window.bind('<B1-Motion>', func3)
window.mainloop()

