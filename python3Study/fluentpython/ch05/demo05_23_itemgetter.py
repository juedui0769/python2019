# 示例 5-23 演示使用 itemgetter 排序一个元组列表（数据来自示例2-8）
from operator import itemgetter
from fluentpython.ch05.ch05_metro_data import get_metro_data

metro_data = get_metro_data()

def test02():
    print('-'*12)
    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print(cc_name(city))

def test01():
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)

def main():
    test01()
    test02()

if __name__ == '__main__':
    main()