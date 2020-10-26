import  tkinter
window = tkinter.Tk()              #创建tkinter对象
window.title('标题')
window.geometry('200x200')          #设置窗口大小
#创建一个顶级菜单栏
menubar = tkinter.Menu(window)
#为每个子菜单实例添加菜单项
#创建文件菜单项，并添加子菜单
fmenu = tkinter.Menu(menubar)
for each in ['新建', '打开', '保存', '另存为']:
    fmenu.add_command(label = each)
#创建视图菜单项，并添加子菜单
vmenu = tkinter.Menu(menubar)
for each in ['复制', '粘贴', '剪切']:
    vmenu.add_command(label = each)
    #创建编辑菜单项
emenu = tkinter.Menu(menubar)
for each in ['默认试图', '新式试图']:
    emenu.add_command(label = each)
#创建关于菜单项，添加子菜单
amenu = tkinter.Menu(menubar)
for each in ['版权信息', '联系我们']:
    amenu.add_command(label = each)
menubar.add_cascade(label = '文件',menu = fmenu)
menubar.add_cascade(label = '视图',menu = vmenu)
menubar.add_cascade(label = '编辑',menu = emenu)
menubar.add_cascade(label = '关于',menu = amenu)
window.config(menu = menubar)
window.mainloop()
