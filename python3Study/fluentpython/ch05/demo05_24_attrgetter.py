# 示例5-24 定义一个 namedtuple, 名为 metro_data （与示例5-23中的列表相同），演示使用 attrgetter 处理它
from collections import namedtuple
from operator import attrgetter
from fluentpython.ch05.ch05_metro_data import get_metro_data

metro_data = get_metro_data()

LatLong = namedtuple('LatLong', 'lat long') #(1)
Metropolis = namedtuple('Metropolis', 'name cc pop coord') #(2)
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data] #(3)


def test01():
    _obj = metro_areas[0]
    print(_obj)
    _obj = metro_areas[0].coord.lat #(4)
    print(_obj)
    name_lat = attrgetter('name', 'coord.lat') #(5)
    for city in sorted(metro_areas, key=attrgetter('coord.lat')): #(6)
        print(name_lat(city)) #(7)


def test02():
    import operator
    _list = [name for name in dir(operator) if not name.startswith('_')]
    print('-'*20)
    print(_list)
    print(len(_list))


def main():
    test01()
    test02()

if __name__ == '__main__':
    main()