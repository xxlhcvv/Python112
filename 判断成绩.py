while True:
    user_input=input('请输入你的成绩：')
    if user_input.upper()=='Q':
        print('计算结束！')
        break
    score=int(user_input)
    if 85 <= score <= 100:
        print('优秀')
    elif 60 <= score < 85:
        print('及格')
    elif 0 <= score < 60:
        print('不及格')
    else:
        print("成绩输入无效，请输入0~100之间的数字")



