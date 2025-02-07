# 定义一个列表
list1 = [1, 2, 3, 4, 5, 6]

# 1.添加元素
print(list1)  # [1, 2, 3, 4, 5, 6]
list1.insert(0, 0)
print(list1)  # [0, 1, 2, 3, 4, 5, 6]

# 2.合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1))  # 9

# 3.先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
print(list1)  # [0, 1, 2, 4, 5, 6, 1000, 2000]

# 4.从指定的位置删除元素
list1.pop(0)
print(list1)  # [1, 2, 4, 5, 6, 1000, 2000]
list1.pop(len(list1) - 1)
print(list1)  # [1, 2, 4, 5, 6, 1000]

# 5.清空列表
list1.clear()
print(list1)  # []

fruits = ['grape', 'apple']
fruits += ['pear', 'mango']
# 6.列表切片
fruits2 = fruits[1:4]
print(fruits2)  # ['apple', 'pear', 'mango']

# 7.可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)  # ['grape', 'apple', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4)  # ['apple', 'pear']

# 8.可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)  # ['mango', 'pear', 'apple', 'grape']

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# 9.sorted函数返回列表排序后的拷贝不会修改传入的列表
list2 = sorted(list1)

# 10.函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)

# 11.通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)

# 12.给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)
