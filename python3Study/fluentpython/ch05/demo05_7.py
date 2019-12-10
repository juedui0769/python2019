fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


def test01():
    _list = sorted(fruits, key=lambda word: word[::-1])
    print(_list)


def main():
    test01()


if __name__ == '__main__':
    main()