# BMI公式：体重除以身高的平方
weight = 78.5
height = 1.74
BMI = weight / (height*height)
print(BMI)
if BMI < 18.5:
    print('过轻')
elif BMI >= 18.5 and BMI < 25:
    print('正常')
elif BMI >= 25 and BMI < 28:
    print('过重')
elif BMI >= 28 and BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
