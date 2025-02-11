class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')



# 属性和方法的访问权限有两种，公开的,私有的。
# 如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
def main():

    # test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    # test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    # print(test.__foo)

    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)

if __name__ == "__main__":
    main()