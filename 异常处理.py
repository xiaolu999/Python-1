try:
    #可能引发的异常代码块
except Exception1:
    #处理异类型一的代码块
except Exception2:
    #处理异常类型二的代码块
。。。
else:
    #如果try子句中的代码块没有引发异常，则执行该代码块
finally:
    #无论try子句中的代码块有没有引发异常，都会执行的代码块