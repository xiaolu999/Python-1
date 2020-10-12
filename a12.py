import random
s=random.randint(0,20)
for i in range(5):
    guess = int(input('你猜一下这个数字是多少0到20之间'))
    if guess<s:
        print('你猜小了')
    elif guess>s:
        print('你猜大了')
    else:
        print('你猜对了')
else:
    print('这个数字是：',s)
    print('你没机会了')