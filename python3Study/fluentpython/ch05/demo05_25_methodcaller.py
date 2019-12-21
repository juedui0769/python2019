# 示例5-25 mthodcaller 使用示例： 第二个测试展示绑定额外参数的方式
from operator import methodcaller

s = 'The time has come'

def test01():
    func_uppercase = methodcaller('upper')
    _obj = func_uppercase(s)
    print(_obj)
    _func = methodcaller('replace', ' ', '-')
    _obj = _func(s)
    print(_obj)

def test02():
    _obj = str.upper(s)
    print(_obj)

def main():
    test01()
    test02()

if __name__ == '__main__':
    main()