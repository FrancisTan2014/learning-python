# 递归函数：求阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))
print(fact(100))

# 递归函数：汉诺塔
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n-1, a, c, b) # 先将n-1个盘子借助c，从a移动到b
        print(a, '-->', c) # 将原来a上的最下面一个盘子移动到c
        hanoi(n-1, b, a, c) # 最后将b上面的n-1个盘子借助a移动到c

hanoi(4, 'A', 'B', 'C')