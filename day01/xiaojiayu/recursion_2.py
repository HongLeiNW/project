#斐波那契数列的迭代实现--n1+n2=n3
#相应速度快
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    #不能输入0或负数
    if n < 1:
        print('输入错误！')
        return -1

    while (n - 2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return n3

result = int(input('Input one number: '))
fab_number = fab(result)
if result != -1:
    print('数量共计 %d 个' % fab_number)