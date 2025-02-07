# 1. for-in循环: 如果明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到），那么我们推荐使用for-in循环。
#   1.1 用for循环实现1~100之间的偶数求和
from itertools import count

sum = 0
for x in range(101):
    sum += x
print(sum)  # 5050
# 说明：上面代码中的range(1, 101)可以用来构造一个从1到100的范围，当我们把这样一个范围放到for-in循环中，就可以通过前面的循环变量x依次取出从1到100的整数。
#     - range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
#     - range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
#     - range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
#     - range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

#   1.2 用for循环实现1~100之间的偶数求和
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)  # 2550

#   1.3 用for循环实现1~100之间的偶数求和
sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)  # 2550


# 2. while循环: 如果要构造不知道具体循环次数的循环结构，推荐使用`while`循环。`while`循环通过一个能够产生或转换出`bool`值的表达式来控制循环，表达式的值为`True`则继续循环；表达式的值为`False`则结束循环。
#   2.1 猜数字游戏
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')

#   2.2 输出乘法口诀表(九九表)
#       和分支结构一样，循环结构也是可以嵌套的，也就是说在循环中还可以构造循环结构。下面的例子演示了如何通过嵌套的循环来输出一个九九乘法表。
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()


# 3. 练习
#   3.1 输入一个正整数判断是不是素数：素数指的是只能被1和自身整除的大于1的整数。
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

#   3.2 输入两个正整数，计算它们的最大公约数和最小公倍数。
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1): # 可以产生x到1的降序整数序列，每次减1
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

#   3.3 打印三角形图案
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
