from fluentpython.ch05.ch05_clip import clip

# 示例5-16 提取关于函数参数的信息
def test01():
    _obj = clip.__defaults__
    print(_obj)
    _obj = clip.__code__
    print(_obj)
    _obj = clip.__code__.co_varnames
    print(_obj)
    _obj = clip.__code__.co_argcount
    print(_obj)



def main():
    test01()


if __name__ == '__main__':
    main()