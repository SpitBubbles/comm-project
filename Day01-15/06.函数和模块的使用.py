# 0. 引入：输入M和N计算C(M,N)，在代码中，我们做了3次求阶乘，这样的代码实际上就是重复代码
m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fm_n = 1
for num in range(1, m - n + 1):
    fm_n *= num
print(fm // fn // fm_n)


# 1. 定义函数
def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(fac(m) // fac(n) // fac(m - n))

# 2. 函数的参数
#     2.1 传参以及参数的重载
from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


#   2.2 可变参数
#       我们可能会对0个或多个参数进行加法运算，而具体有多少个参数是由调用者来决定，我们作为函数的设计者对这一点是一无所知的，因此在不确定参数个数的时候，我们可以使用可变参数。
#       在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))


# 3. 模块化管理函数
# module1.py
def foo():
    print('hello, world!')


# module2.py
def foo():
    print('goodbye, world!')


# test.py
# from module1 import foo # 导入module1中的foo函数
# 输出hello, world!
foo()

# from module2 import foo # 导入module2中的foo函数
# 输出goodbye, world!
foo()


# import module1 as m1
# import module2 as m2

# m1.foo() # 输出hello, world!
# m2.foo() # 输出goodbye, world!


# 4. 隐含的变量
#   如果我们导入的模块除了定义函数之外还有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
#   事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，
#   这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是"__main__"。
def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()


# 5. 练习
#   5.1 实现计算求最大公约数和最小公倍数的函数。
def max_common_divisor(a, b):
    """求最大公约数"""
    if a > b:
        a, b = b, a
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
def min_common_multiple(a, b):
    """求最小公倍数"""
    return a * b // max_common_divisor(a, b)


#   5.2 实现判断一个数是不是回文数的函。
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num




