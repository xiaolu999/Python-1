password = ''  # 变量password用来保存输入的密码
i = 0
while True:
    password = input('请尝试输入密码')
    if password != '816':
        if  i <= 3:
            i = i + 1
            print('密码不对')
        else:
            print('解锁已达最大次数')
            break
    else:
        print('欢迎回家')
        break


