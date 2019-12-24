# 7-6

from dis import dis
from fluentpython.ch07.demo7_4 import f1
if __name__ == '__main__':
    _obj = dis(f1)
    print(_obj)
