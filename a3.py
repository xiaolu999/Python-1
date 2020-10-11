score = int(input('请输入你的成绩:'))
for s in range(1,4):
    if score>=60:
        if score>=80:
            print('你很优秀')
        else:
            print('你只是一般般')
    else:
        print('不及格了')
        if score <30:
            print('学渣')
        else:
            print('还能抢救一下')