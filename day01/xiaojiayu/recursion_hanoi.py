#汉诺塔递归实现
def hanoi(n, x, y, z):
    if n == 1:
        print(x, '--->', z)
    else:
        #n-1从x移动到y
        hanoi(n-1, x, z, y)
        #x柱子上最大的盘子由x到z
        print(x, '--->', z)
        #y柱子上n-1盘子移动到z
        hanoi(n-1, y, x, z)

n = int(input('Input Hanoi number: '))
hanoi(n, 'x', 'y', 'z')
