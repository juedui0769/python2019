
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

fact = factorial

def test01():
    _list = list(map(fact, range(6)))
    print(_list)
    _list = [fact(n) for n in range(6)]
    print(_list)
    _list = list(map(factorial, filter(lambda n: n % 2, range(6))))
    print(_list)
    _list = [factorial(n) for n in range(6) if n % 2]
    print(_list)


def main():
    test01()


if __name__ == '__main__':
    main()