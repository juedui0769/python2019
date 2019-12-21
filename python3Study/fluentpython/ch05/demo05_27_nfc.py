# 示例5-27
import unicodedata, functools
def main():
    nfc = functools.partial(unicodedata.normalize, 'NFC')
    s1 = 'café'
    s2 = 'cafe\u0301'
    _tuple = s1, s2
    print(_tuple)
    _bool = s1 == s2
    print(_bool)
    _bool = nfc(s1) == nfc(s2)
    print(_bool)
if __name__ == '__main__':
    main()