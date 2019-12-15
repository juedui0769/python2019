def test01():
    _tuple = abs, str, 13
    print(_tuple)
    _list = [callable(obj) for obj in _tuple]
    print(_list)


def main():
    test01()


if __name__ == '__main__':
    main()