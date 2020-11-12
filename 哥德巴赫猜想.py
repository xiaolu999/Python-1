def prime(i):						#定义函数，判断i是否为素数
    if i<=1:						#如果小于等于1，返回0（i不是素数）
        return 0
    if i==2:						#如果等于2，返回1（i是素数）
        return 1
    for j in range(2,i):				#判断i是否为素数
        if i%j==0:				#i可以被j除尽，余数为0
            return 0				#返回0，i不是素数
        elif i!=j+1:				#如果i不等于j+1，继续
            continue
        else:
            return 1				#否则，i等于j+1，返回1（i是素数）
n=0
for i in range(6,21,2):
    k=2
    while k<=i/2:
        j=i-k
        flag1=prime(k)			#调用prime函数
        if flag1:					#如果k为素数
            flag2=prime(j)			#调用prime函数
            if flag2:				#如果k和j都是素数
                print(i,'=',k,'+',j)	#输出结果
                n+=1
        k=k+1
