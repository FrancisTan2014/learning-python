# python中的切片操作：取数组中指定范围的元素
# 需要注意的是：这种操作得到的结果包含左边不包含右边
arr = [1, 2, 3, 4, 5]
a1 = arr[0:3]
print('arr[0:3]\n', a1)
a2 = arr[:2]
print('arr[:2]\n', a2)
a3 = arr[2:5]
print('arr[2:5]\n', a3)

# 切片高级应用
arr = list(range(100)) # 创建一个0到99的数列
print('数组的前十个元素arr[:10]\n', arr[:10])
print('数组的后10个元素arr[-10:]\n', arr[-10:])
print('数组的前11到20个元素arr[10:20]\n', arr[10:20])
print('前十个数，每隔两个取一个arr[:10:2]\n', arr[:10:2])
print('所有的数，每隔五个取一个arr[::5]\n', arr[::5])
print('什么都不写，可直接复制一个数组arr[:]\n', len(arr[:]))

# 字符串也可以用切片，相当于其他语言的replace，不过比之更灵活
s = 'abcdefghijklmnopqrstuvwxyz'
print('s[:10]: %s' % s[:10])
print('s[-10:]: %s' % s[-10:])