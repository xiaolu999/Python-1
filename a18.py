def prime(i):
    if i <= 1:
        return 0
    if i == 2:
        return 1
    for j in range(2, i):
        if i % j == 0:
            return 0
        elif i != j+1:
            continue
        else:
            return 1
n=0
for i in range(6,21,2):
    k = 2
    while k <= i/2:
        j=i-k
        flag1 = prime(k)
        if flag1:
            flag2 = prime(j)
            if flag2:
                print(i,'=',k,'+',j)
                n +=1
        k=k+1
