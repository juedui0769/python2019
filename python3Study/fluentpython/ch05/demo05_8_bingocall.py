import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items) #(1)
        random.shuffle(self._items) #(2)

    def pick(self): #(3)
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage') #(4)

    def __call__(self, *args, **kwargs): #(5)
        return self.pick()



def test01():
    bingo = BingoCage(range(3))
    _ret = bingo.pick()
    print(_ret)
    _ret = bingo()
    print(_ret)
    _ret = callable(bingo)
    print(_ret)


def main():
    test01()


if __name__ == '__main__':
    main()