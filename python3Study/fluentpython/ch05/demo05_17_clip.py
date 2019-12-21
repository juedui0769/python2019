from fluentpython.ch05.ch05_clip import clip
from inspect import signature

# 示例5-17 提取函数的签名
def test01():
    sig = signature(clip)
    print(sig)
    _obj = repr(sig)
    print(_obj)
    _obj = str(sig)
    print(_obj)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)


def main():
    test01()

if __name__ == '__main__':
    main()