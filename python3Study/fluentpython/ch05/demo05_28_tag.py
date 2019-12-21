# 示例5-28
from fluentpython.ch05.ch05_tag import tag
from functools import partial
def main():
    _obj = repr(tag)
    print(_obj)
    picture = partial(tag, 'img', cls='pic-frame') #(2)
    _html = picture(src='wumpus.jpeg')
    print(_html)
    _obj = repr(picture)
    print(_obj)
    _obj = picture.func #(5)
    print(_obj)
    _obj = picture.args
    print(_obj)
    _obj = picture.keywords
    print(_obj)
if __name__ == '__main__':
    main()