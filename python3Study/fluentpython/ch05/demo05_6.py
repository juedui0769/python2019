
from functools import reduce
from operator import add

def test01():
    _val = reduce(add, range(100))
    print(_val)
    _val = sum(range(100))
    print(_val)


def main():
    test01()


if __name__ == '__main__':
    main()