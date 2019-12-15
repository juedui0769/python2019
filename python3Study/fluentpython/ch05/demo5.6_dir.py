def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n-1)


def test01():
    _dir = dir(factorial)
    print(_dir)


def main():
    test01()


if __name__ == '__main__':
    main()