class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}只能观看《熊出没》.')
        if self.age >= 18:
            print(f'{self.name}正在观看《Python 100 Day》.')


def main():
    stu1 = Student('派森', 10)
    stu1.study('Python 程序设计')
    stu1.watch_movie()
    stu2 = Student('赛嘉嘉', 20)
    stu2.study('C++ 程序设计')
    stu2.watch_movie()

    if __name__ == '__main__':
        main()
