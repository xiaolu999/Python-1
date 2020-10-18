file = open('testfile.txt','w')
file.write('123456789adsasdad\n')
file.write('nishishanizade\n')
file.close()
#追加
Is = ['147258369\n','nimeishiba ']
with open('testfile.txt','a')as file:
    file.writelines(Is)