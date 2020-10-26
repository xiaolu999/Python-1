from tkinter import *
root = Tk()
def hello():
    print('选择了菜单！')
root.geometry('200x100')             #设置窗口大小

#创建一个顶级菜单实例


menu = Menu(root)
menu.add_command(label='显示', command =hello)
menu.add_command(label = '退出', command = root.quit)
#弹出菜单
frame = Frame(root, width = 512, height = 512)
frame.pack()


#定义函数，调用post()方法显示
def popup(event):
    menu.post(event.x_root, event.y_root)


#绑定鼠标右键

frame.bind('<Button-3>', popup)
root.config(menu = menu)        #显示菜单
root.mainloop()
