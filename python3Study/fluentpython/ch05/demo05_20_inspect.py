from fluentpython.ch05.ch05_clip_v2 import clip
from inspect import signature

# 示例5-20 从函数签名中提取注解
def main():
    sig = signature(clip)
    _obj = sig.return_annotation
    print(_obj)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)


if __name__ == '__main__':
    main()