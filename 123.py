list_lines = ['一弦一柱思华年。\n','只是当时已惘然。\n']
while True:
    with open('poem.txt','r', encoding='utf-8') as f:
        lines = f.readlines()
    with open('poem.txt', 'w', encoding='utf-8') as m:
        for new in lines:
            if new in list_lines:
                m.write('____________\n')
            else:
                m.write(new)
            s = input('是否继续:1 结束，其他继续')
            if s=='1':
                break
            else:
                gg = input('请输入想要考察的句子')
                list_lines.pop()
                print(list_lines)
                list_lines.append(gg)
                print(list_lines)
                print('继续')


