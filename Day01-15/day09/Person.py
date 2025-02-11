# 使用 @property 包装器来包装 getter 和 setter 方法
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 -- getter方法
    @property
    def name(self):
        return self._name

    # 访问器 -- getter方法
    @property
    def age(self):
        return self._age

    # 修改器 -- setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person = Person('王大锤', 12)
    print(person.name)
    print(person.age)
    person.play()
    print('===============')
    person.age = 22
    print(person.name)
    print(person.age)
    person.play()

if __name__ == '__main__':
    main()