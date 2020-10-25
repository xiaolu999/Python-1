import tkinter as tk

def btnHelloClicked():
    cd = float(entryCd.get())
    labelHello.config(text='%.2f℃ = %.2f℉' %(cd,cd*1.8+32))

top = tk.Tk()
top.title('EntryText')
#创建标签
labelHello = tk.Label(top,text = '摄氏度转华氏度', height=5, width=20, fg = 'blue')
labelHello.pack()
entryCd = tk.Entry(top,text = '0')
entryCd.pack()
btnCal = tk.Button(top, text = '计算', command = btnHelloClicked)
btnCal.pack()
top.mainloop()
