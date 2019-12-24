# 7-7
from dis import dis
# from fluentpython.ch07.demo7_5 import f2

b = 6
def f2(a):
    print(a)
    # UnboundLocalError: local variable 'b' referenced before assignment
    print(b)
    b = 9

if __name__ == '__main__':
    _obj = dis(f2)
    print(_obj)