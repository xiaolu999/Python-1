import math
while True:
    a = int(input('请输入三角形的第一条边:'))
    b = int(input('请输入三角形的第二条边:'))
    c = int(input('请输入三角形的第三条边:'))
    if a>0and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
        s=1/2*(a+b+c)
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print('三角形的面积是:',area)
    else:
        print('不能构成三角形')
    a = input('是否重新输入,输入S结束运行')
    if a=='l':
        break