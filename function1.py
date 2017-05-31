# 可变参数函数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2))
print(calc(1, 2, 3, 4))

arr = [4, 5, 6, 7, 8, 9]
print(calc(*arr))