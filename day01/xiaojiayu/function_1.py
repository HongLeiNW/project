
#定义函数
def factorial(n):
    #赋值，用于循环，此处result被shadowing
    result = n
    #以n为条件循环相乘求阶乘
    for i in range(1, n):
        result *= i
    #返回函数的值
    return result

#定义一个变量，获取输入的值
number = int(input('Input one number: '))
#调用函数并赋值给变量，注意，此变量result与函数factorial中的result不是同一个变量
result = factorial(number)
#格式化输出
print('%d 的阶乘是: %d ' % (number, result))
