
def f(a, *, b):
    return a, b

def test01():
    _ret = f(1, b=2)
    print(_ret)
    # 下面的语句会报错：  TypeError: f() takes 1 positional argument but 2 were given
    _ret = f(1, 2)
    print(_ret)


def main():
    test01()


if __name__ == '__main__':
    main()