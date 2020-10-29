import random
while True:
    punchs = ['石头', '剪刀', '布']
    computer_choice = random.choice(punchs)
    user_choice = input('请输入石头剪刀布')
    while user_choice not in punchs:
        print('请重新输入')
        user_choice = input()


    print('---------开始---------')
    print('你出了%s'%(user_choice))
    print('电脑出了%s'%(computer_choice))

    print('-----结果是-----')
    if user_choice==computer_choice:
        print('平局了')
    elif (user_choice == '石头' and computer_choice == '剪刀') or (user_choice == '剪刀'and computer_choice == '布') or (user_choice == '布' and computer_choice == '石头'):
        print('你赢了')
    else:
        print('你输了')
    s = input('是否继续')
    if s == '继续':
        print('继续')
    else:
        break
