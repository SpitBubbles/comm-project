# 在屏幕上显示跑马灯文字
import os
import time


def main():
    count = 0;
    content = '北京欢迎你为你开天辟地…………'
    while count <= 20:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]
        count += 1


if __name__ == '__main__':
    main()
