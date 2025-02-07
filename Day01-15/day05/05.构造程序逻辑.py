# 1. 寻找水仙花数:水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：1^3 + 5^3+ 3^3=153。
for i in range(100, 1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100
    if i == low ** 3 + mid ** 3 + high ** 3:
        print(i)

# 2. 正整数的反转
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = num % 10 + reversed_num * 10
    num //= 10
print(reversed_num)

# 3. 百钱百鸡问题：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for i in range(0, 20):
    for j in range(0, 33):
        z = 100 - i - j
        if 5 * i + 3 * j + z / 3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (i, j, z))

# 4. CRAPS赌博游戏：该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
#       玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
#       玩家第一次如果摇出2点、3点或12点，庄家胜；
#       其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
#       如果玩家摇出了第一次摇的点数，玩家胜；
#       其他点数，玩家继续要骰子，直到分出胜负。
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')

# 5. 生成斐波那契数列的前20个数
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
