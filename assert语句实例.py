while True:
    try:
        score = int(input('请输入百分制成绩：'))
        assert score >= 0 and score <=100, '分数必须是1~100之间'
        if score>=90:
            print('优')
        elif score>=80:
            print('良')
        elif score>=70:
            print('youxiu')
        elif score>=60:
            print('及格')
        else:
            print('不及格')
    except Exception as r:
        print('发生异常',r)
        break
