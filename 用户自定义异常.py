class SexException(Exception):
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value
def f():

    sex = input('请输入性比别')

    if sex != '男' and sex !='女':

        raise SexException('性别只能是男或者女', sex)
try:
    f()
except Exception as ex:
    print('错误信息：%s,请输入性别是；%s' %(ex.msg, ex.value))