import tkinter


def callback():
    print('单击了；‘显示’菜单')


window = tkinter.Tk()
window.title('标题')
window.geometry('200x200')
menubar =tkinter.Menu(window)
menubar.add_command(label = '显示', command = callback)
menubar.add_command(label = '显示', command = window.quit)
window.config(menu = menubar)
window.mainloop()