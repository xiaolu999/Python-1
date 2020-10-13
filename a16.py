data = {'北京':
        {'昌平':
             {'沙河':['沙河机场','链家'],
              '天通苑':['北方明珠','天通尾货']},

        '朝阳':
            {'花家地':['朝阳公园','望京SOHO'],
             '北小河':['北小河公园','北京中学']}},

    '上海':
        {'虹桥':
             {'虹桥机场':['超市','特产店','水吧'],
              '东方明珠':['电影院','游泳馆','餐馆']},

          '浦东':
              {'景秀路':['世纪公园','立交桥'],
               '中环路':['鲁迅公园','同济大学']}},

    '河北':
        {'石家庄':
             {'行唐':['东正','阳关'],
              '赵县':['赵州桥','高村乡']},

          '唐山':
              {'滦南县':['司各庄镇','安各庄镇'],
               '玉田县':['玉田镇','亮甲店镇']}}}
while True:
    for i in data:
        print(i)
    choice = input('请选择省或者直辖市（退出请按q）')
    if choice in data:
        while True:
            for i2 in data[choice]:
                print(i2)
            choice2 = input('请选择(退出请按q返回上一级请按m)')
            if choice2 in data[choice]:
                while True:
                    for i3 in data[choice][choice2]:
                        print(i3)
                    choice3 = input('请选择(退出请按q返回上一级请按m)')
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input('已经是最后一个了，退出请按q，返回上一级请按m')
                        if choice4 == 'm':
                            continue
                        elif choice == 'q':
                            exit()
                    elif choice3 == 'm':
                        break
                    elif choice3 == 'q':
                        exit()
            elif choice2 == 'm':
                break
            elif choice2 == 'q':
                exit()
    elif choice == 'q':
        exit()



