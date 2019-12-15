def test01():
    class C: pass #(1)
    obj = C() #(2)
    def func(): pass #(3)
    _ret = sorted(set(dir(func)) - set(dir(obj)))
    print(_ret)


def main():
    test01()


if __name__ == '__main__':
    main()