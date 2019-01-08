#斐波那契数列递归实现--n1+n2=n3
#效率较慢
def fab(n):
    #限制不能为0或负数
    if n < 1:
        print('输入错误！')
        #返回值
        return -1
    #第一和第二默认为1
    if n == 1 or n == 2:
        return 1
    #从3开始运行相加
    else:
        return fab(n-1) + fab(n-2)

number = int(input('Input one number: '))
result = fab(number)
if result != 1:
    print('数量共计 %d 个' % result)
