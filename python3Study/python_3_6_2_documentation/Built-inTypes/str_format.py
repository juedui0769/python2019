def test01():
    _str = "The sum of 1 + 2 is {0}".format(1+2)
    print(_str)

class Default(dict):
    def __missing__(self, key):
        return key


def test02():
    _str = "{name} was born in {country}".format_map(Default(name='Guido'))
    print(_str)
    _str = "{name} was born in {country}".format_map(Default(country='China'))
    print(_str)
    _str = "{name} was born in {country}".format_map(Default(name='Guido', country='China'))
    print(_str)


def main():
    test01()
    test02()


if __name__ == '__main__':
    main()