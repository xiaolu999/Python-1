user_name = input('请输入用户名以_开头，3-30个字符')
password = input('请输入密码，有下划线数字和字母组成，8-16个字符')
if user_name[0]!='_':
    print('请使用后下划线开头')
elif 3>len(user_name)or len(user_name)>30:
    prinrt('用户名超出限制')
elif len(password)<8 or len(password)>16:
    print('密码长度超出限制')
elif password.find('_')==-1:
    print('密码中青输入下划线')
else:
    password = password.replace('_','1')
    if password.isalnum():
        print('恭喜您注册成功用户名:',user_name,'密码是:',password)
    else:
        print('密码中有其他符号，注册失败')