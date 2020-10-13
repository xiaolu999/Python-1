count = 0z
password = 123
dict1 = {'alex':[password,count],'tom':[password,count]}
while True:
    name = input('请输入你的名字')
    password = int(input('请输入你的密码'))
    if name not in dict1.keys():
        print('你输入的名字{0}不在列表了'.format(name ))
        break
    if dict1[name][1]>2:
        print('这个名字{0}被锁住了'.format(name))
        #continue
        break
    if password == dict1[name][0]:
        print('登陆成功')
        break
    else:
        print('用户名或密码错误')
        dict1 [name][1] += 1