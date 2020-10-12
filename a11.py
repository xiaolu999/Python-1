import random
i=1
s=random.randint(0,10)
while True:
    if i<=3:
        guess =int(input('你猜这个数字是多少0到10之间'))
        i=i+1
        if guess>s:
            print('你猜大了')
        elif guess<s:
            print('你才小了')
        else:
            print('你猜对了')
    else:
        print('这个数是：',s)
        print('你没机会了')
        break


