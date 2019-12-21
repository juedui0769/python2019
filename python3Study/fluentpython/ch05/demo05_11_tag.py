# import ./tag

import sys
from fluentpython.ch05.ch05_tag import tag

def test01():
    # _html = tag('br')
    _path = sys.path
    print(_path)
    # import ch05_tag
    _html = tag('br')
    print(_html)


def test02():
    _html = tag('br') #(1)
    print(_html)
    _html = tag('p', 'hello') #(2)
    print(_html)
    _html = tag('p', 'hello', 'world')
    print(_html)
    _html = tag('p', 'hello', id=33) #(3)
    print(_html)
    _html = tag('p', 'hello', 'world', cls='sidebar') #(4)
    print(_html)
    _html = tag(content='testing', name='img') #(5)
    print(_html)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    _html = tag(**my_tag) #(6)
    print(_html)


def main():
    test02()


if __name__ == '__main__':
    main()