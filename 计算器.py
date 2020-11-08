import tkinter, time, decimal, math, string
window = tkinter.Tk()
window.title('计算器')
window.resizable(0, 0)
#全局变量， storage 存储列表，vartext 存储字符串， reslut存储结果， symbol存储符号

global storage, vartext, result, symbol
result = symbol = None
vartext = tkinter.StringVar()
storage = []


#按键值类
class key_press:
    global storage, vartext, result, symbol

    #构造方法
    def __init__(self, anjian):
        self.key = anjian

    #添加，用于将案件值添加到storage列表，再讲storage的值设置为vartext的值
    def jia(self):
        storage.append(self.key)    #将按键值添加到storage 列表
        vartext.set(''.join(storage))   #将storage 的值链接生成一个新的字符串，并设置为vartext的值

    # 设置删除功能
    def retreat(self):
        storage.pop()                        #移除storage列表的值（默认最后一个元素）
        vartext.set(''.join(storage))             #将storage的值链接生成一个新的字符串，并设置为vartext的值

    #清除功能
    def clear(self):
        storage.clear()                         #清空storage 列表
        vartext.set('')                           #设置storage的值为空
        result = None                            #将变量result结果改为None
        symbol = None                            #变量symbol结果改为None


    #切换正负功能
    def plus_minus(self, storage):
        if storage[0]:
            if storage == '-':
                storage = '+'
            elif storage[0] == '+':
                storage = '-'
            else:
                storage.insert(0, '-')   #如果storage[0]的 hij9ibushi'+'，又不是‘-’，则表示没有符号，添加一个‘-’
        vartext.set(''.join(storage))     #将storage的值链接生成一个新的字符串，并设置为vartext的值


    #添加小数点的功能
    def decimal_point(self):
        if storage.count('.')>=1:       #如果已将存在小数点则什么都不做
            pass
        else:
            if storage == []:             #如果storage为空
                storage.append('0')       #给storage队列添加0
            storage.append('.')           #给storage队列添加  .
            vartext.set(''.join(storage))    #将storage 的值连接生成一个新的字符串，并设置为vartext的值



    #运算
    def operation(self):
        global stprage, vartext, result, symbol     #引用全局变量
        if vartext.get() == '':                       #如果vartext总没有值，则什么也不做
            pass
        else:
            get1 = decimal.Decimal(vartext.get())         #获取输入的值
            if self.key in ('1/x','sqrt'):                   #如果按键值属于‘1/x’和‘sqrt’之一
                if self.key == '1/x':                         #如果按键值是‘1/x’
                    result = 1/get1                          #将1/get的结果赋值给变量result
                elif self.key == 'sqrt':                       #如果按键值是sqrt
                    result = math.sqrt(get1)                  #计算变量get1的平方根
            elif self.key in ('+','-', '*','/', '='):
                if symbol is not None:
                    get1 =decimal.Decimal(result)
                    get2 = decimal.Decimal(vartext.get())
                    if symbol == '+':
                        result = get1 + get2
                    elif symbol == '-':
                        result = get1 - get2
                    elif symbol == '*':
                        result = get1*get2
                    elif symbol == '/':
                        result = get1/get2
                else:
                    result = get1
                if self.key == '=':
                    symbol = None
                else:
                    symbol = self.key
            print(symbol)
            print(result)
            vartext,set(str(result))
            storage.clear()


#计算器布局

def layout(window):
    global storage, vartext, result, symbol
    #设置顶部标签，用于展示按键的值
    entry1 = tkinter.Label(window, width = 40, height = 3, bg = 'white', anchor = 'se', textvariable = vartext )
    entry1.grid(row = 0,coolumnspan = 5)

    #添加按钮
    buttonJ = tkinter.Button(window, text = '←', width = 5, command = key_press('c').retreat)
    buttonCE = tkinter.Button(window, text = '', width = 5)
    buttonC = tkinter.Button(window, text = 'C', width = 5, command = key_press('c').clear)
    buttonl2 = tkinter.Button(window, text = '±', width = 5, command = key_press('c').plus_minus)
    buttonD = tkinter.Button(window, text = '√', width = 5, command = key_press('sqrt').operation)
    buttonJ.grid(row=2, column=0)
    buttonCE.grid(row=2, column=1)
    buttonC.grid(row=2, column=2)
    buttonl2.grid(row=2, column=3)
    buttonD.grid(row=2, column=4)
    button7 = tkinter.Button(window, text='7', width=5, command=key_press('7').jia)
    button8 = tkinter.Button(window, text='8', width=5, command=key_press('8').jia)
    button9 = tkinter.Button(window, text='9', width=5, command=key_press('9').jia)
    buttonc = tkinter.Button(window, text='/', width=5, command=key_press('/').operation)
    buttonf = tkinter.Button(window, text=' ', width=5)
    button7.grid(row=3, column=0)
    button8.grid(row=3, column=1)
    button9.grid(row=3, column=2)
    buttonc.grid(row=3, column=3)
    buttonf.grid(row=3, column=4)
    button4 = tkinter.Button(window, text='4', width=5, command=key_press('4').jia)
    button5 = tkinter.Button(window, text='5', width=5, command=key_press('5').jia)
    button6 = tkinter.Button(window, text='6', width=5, command=key_press('6').jia)
    buttonx = tkinter.Button(window, text='*', width=5, command=key_press('*').operation)
    buttonfs = tkinter.Button(window, text='1/x', width=5, command=key_press('1/x').operation)
    button4.grid(row=4, column=0)
    button5.grid(row=4, column=1)
    button6.grid(row=4, column=2)
    buttonx.grid(row=4, column=3)
    buttonfs.grid(row=4, column=4)
    button1 = tkinter.Button(window, text='1', width=5, command=key_press('1').jia)
    button2 = tkinter.Button(window, text='2', width=5, command=key_press('2').jia)
    button3 = tkinter.Button(window, text='3', width=5, command=key_press('3').jia)
    button_ = tkinter.Button(window, text='-', width=5, command=key_press('-').operation)
    buttondy = tkinter.Button(window, text='\n = \n', width=5, command=key_press('=').operation)
    button1.grid(row=5, column=0)
    button2.grid(row=5, column=1)
    button3.grid(row=5, column=2)
    button_.grid(row=5, column=3)
    buttondy.grid(row=5, column=4,rowspan=2)
    button0 = tkinter.Button(window, text = '0', width=11, command = key_press('0').jia)
    buttonjh = tkinter.Button(window, text = '.', width=5, command=key_press('c').decimal_point)
    buttonjia = tkinter.Button(window, text = '+', width=5, command = key_press('+').operation)
    button0.grid(row = 6, column=0, columnspan=2)
    buttonjh.grid(row=6, column=2)
    buttonjia.grid(row=6, column=3)

layout(window)
window.mainloop()








