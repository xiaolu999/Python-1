stuInfos = []


def printMenu():
    print('='*20)
    print('学生管理系统v2.0')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.显示所有学生信息')
    print('4.保存数据')
    print('5.恢复系统')
    print('0.退出系统')
    print('='*20)


def addStuInfo():
    newNum = input('请输入新学生的学号')
    newName = input('请输入新学生的姓名')
    newSex = input('请输入新学生的性别（男/女）:')
    newInfo = {}
    newInfo['num'] = newNum
    newInfo['name'] = newName
    newInfo['sex'] = newSex
    stuInfos.append(newInfo)


def delStuInfo():
    del_num = input('请输入要删除的学号')
    for stu in stuInfos:
        if stu['num'] == del_num:
            print('删除成功')
            stuInfos.remove(stu)




def showStuInfo():
    print('='*20)
    print('学生信息如下')
    print('='*20)
    print('序号     姓名     学号     性别     ')
    i=1
    for tempInfo in stuInfos:
        print('%d     %s     %s     %s' % (i, tempInfo['num'], tempInfo['name'], tempInfo['sex']))
        i+=1


def save_file():
    with open('student.txt', 'w')as file:
        file.write(str(stuInfos))


def recover_data():
    global stuInfos
    with open('student.txt', 'r')as file:
        content = file.read()
        stuInfos = eval(content)


def main():
    while True:
        printMenu()
        key = input('请输入对应功能的数字')
        if key =='1':
            addStuInfo()
        elif key == '2':
            delStuInfo()
        elif key == '3':
            showStuInfo()
        elif key == '4':
            save_file()
        elif key == '5':
            recover_data()
        elif key == '0':
            q = input('确定退出吗？(yes or no)')
            if q == 'yes':
                break
main()








