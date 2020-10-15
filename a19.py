stuInfos =[]    #存储学生信息
#打印菜单
def printMenu():
    print('='*20)
    print('学生管理系统')
    print('1添加雪生信息')
    print('2删除学生系统')
    print('3显示所有学生信息')
    print('0退出系统')
#添加学生信息
def addStuInfo():
    newNum = input('请输入学生的学号')
    newName = input('请输入学生的姓名')
    newSex = input('请输入学生的性别')
    newInfo={}
    newInfo['num'] = newNum
    newInfo['Name'] = newName
    newInfo['Sex'] = newSex
    stuInfos.append(newInfo)
#删除学生信息
def delstuInfo():
    del_name = input('请输入要删除的学生的学号')
    for stu in stuInfos:
        if stu['num']==del_name:
            stuInfos.remove(stu)
#显示学生信息
def showstuInfos():
    print('=*20')
    print('学生信息如下')
    print('*'*20)
    print('序号      学号     姓名      性别')
    i=1
    for tempInfo in stuInfos:
        print('{0}       {1}       {2}       {3}'.format(i,tempInfo['num'],tempInfo['Name'],tempInfo['Sex'] ))
        i+=1
#main控制整个过程
def main():
    while True:
        printMenu()
        key = input('请输入功能对应的数字')
        if key=='1':
            addStuInfo()
        if key=='2':
            delstuInfo()
        if key=='3':
            showstuInfos()
        if key=='0':
            quit_con = input('确定退出吗？Y or N:')
            if quit_con=='Y':
                break
main()
