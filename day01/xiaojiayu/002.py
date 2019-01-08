#引入类型判断
import re

#提示内容
print('--------------------分数分类演示--------------------')
#定义变量，用来存储输入的值
score = input('Input your score:')
#判断是否为数字类型
while score.isdigit() == 0:
    #提示输入错误，并重新输入
    score = input('Input worng type,input again:')
else:
    #赋值，浮点型
    score = float(score)
    #判断
    if score == 100:
        print('A+')
    elif 100 > score >= 95:
        print('A')
    elif 95 > score >= 90:
        print('A-')
    elif 90 > score >= 80:
        print('B')
    elif 80 > score >= 70:
        print('C')
    elif 70 > score >= 60:
        print('D')
    elif 60 > score >=0:
        print('E')
print('Over')