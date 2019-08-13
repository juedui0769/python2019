"""
 / list , tuple , collections.deque
 \ str, bytes, bytearray, memoryview, array.array

 / list , bytearray , array.array , collections.deque , memoryview
 \ tuple , str , bytes

 Container , Iterable , Sized , Sequence , MutableSequence
"""

def demo2_1():
    symbols = '$¢£¥€¤'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)

# demo2_1()

def demo2_2():
    symbols = '$¢£¥€¤'
    codes = [ord(symbol) for symbol in symbols]
    print(codes)

# demo2_2()

def after_demo2_2():
    x = 'ABC'
    dummy = [ord(x) for x in x]
    print(x)
    print(dummy)

# after_demo2_2()

def test01():
    # pass
    codes = [36, 162, 163, 165, 8364, 164]
    symbols = [chr(code) for code in codes]
    print(symbols)
    print("".join(symbols))

if __name__ == '__main__' :
    pass
    # print('hello world')
    # test01()