def div(num1,num2):
    growth = (num1-num2)/num2
    percent = str(growth*100)+'%'
    return percent
def warning():
    print('你确定一毛都不赚啊')
def main():
    while True:
        num1 = float(input('请输入本月收入'))
        num2 =float(input('请输入上月收入'))
        if num2==0:
            warning()
            continue
        else:
            print('本月收入增长'+div(num1,num2))
            break
main()