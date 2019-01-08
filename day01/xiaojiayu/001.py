#引入随机生成模块
import random
#引入判断数据类型
import re

print('--------------猜数字小游戏V1.0---------------')
print('-----------------1-9猜数字------------------')
#生成一个随机数1-9
secret = random.randint(1, 9)
#变量赋值，不等于生成的数，此变量作为与随机生成数比较使用
guess = 0
#计数器
count = 0
#循环判断，变量与随机生成数不同时且计数器小于3次开始循环
while guess != secret and count < 3:
    #获取一个输入的值
    temp = input("猜猜看吧，请输入一个数字：")
    #判断输入的值是否为整数，是则继续
    if temp.isdigit():
        #整型赋值
        guess = int(temp)
        #计数器+1
        count += 1
        #判断获取值与生成值是否相等，相等输出下面内容并跳出循环
        if guess == secret:
            print("恭喜你，猜对了！")
            print("Pass Game!")
        #判断大小，并输出提示
        else:
            if guess > secret:
                print('Big')
            else:
                print('Small')
            #判断计数器并输出提示
            if count < 3:
                print('One More Time:')
            #判断计数器并输出提示，如果计数器等于3，跳出循环
            else:
                print('Over Times!')
    #判断输入的值是否为整数，不是输出下列内容并重新开始循环
    else:
        print('Input type wrong,input again:')
print('Game Over')

