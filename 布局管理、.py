from tkinter import *
root = Tk()
root.title('pack举例')
#使用Frame增加一层容器】
fin1 = Frame(root)
#创建3个按钮，从上到下排列
Button(fin1, text = 'Top').pack(side = TOP, anchor = W, fill = X )
Button(fin1, text = 'Center').pack(side = TOP, anchor = W, fill = X )
Button(fin1, text = 'Buttom').pack(side = TOP, anchor = W, fill = X )
fin1.pack(side = LEFT, fill = Y)
#使用frame再增加一个容器
fin2 = Frame(root)
#创建3个按钮，从左到右
Button(fin2, text = 'LEFT').pack(side = LEFT)
Button(fin2, text = 'This is Center button').pack(side = LEFT)
Button(fin2, text = 'Right').pack(side = LEFT)
fin2.pack(side = LEFT, padx = 10)      #与fin1间隔为10
root.mainloop()


