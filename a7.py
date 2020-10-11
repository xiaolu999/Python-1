i = input('您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要')
if i=='需要':
    l=input('请问您需要什么帮助?1存取款2货币兑换,其他键咨询')
    if l=='2':
        h=int(input('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币，请问您需要对换多少'))
        j=h*51.3
        print('您需要支付'+str(j)+'人民币')
    elif l=='1':
        h1 = int(input('您需要存多少钱'))
        cunchu=h1
        print('恭喜您存款'+str(cunchu)+'yuan成功')
    else:
        print('请问您需要咨询啥')
else:
    print('欢迎您下次光临')
