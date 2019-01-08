
#定义一个函数（递归），参数为0停止执行函数，参数*参数-1并返回
def factorial(n):
    if n == 1:
        #递归函数一定要有返回值，否则将无限循环，默认100此递归
        return 1
    else:
        return n * factorial(n-1)

#定义一个变量获取输入的值
number = int(input('Input one number: '))
#定义一个变量，调用函数并赋值
result = factorial(number)
#格式化输出
print('%d 的阶乘是：%d ' % (number, result))
