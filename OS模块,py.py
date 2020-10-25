import os   #导入os模块

os.getcwd()     #显示当前的工作目录
os.mkdir('ostest')   #创建目录
os.chdir('ostest')    #将当前的‘ostest’  目录作为当前的目录
os.mkdir('mktest')         #在目录osetst目录中创建目录mktest
f = open('1.txt', 'w')     #在当前的目录下创建并打开1.txt文件
f.close()                         #关闭文件
os.rename('1.txt', '2.txt')              #重命名文件
os.listdir()                #查看文件和目录列表
os.rmdir()          #删除目录
os.remove()             #删除文件

