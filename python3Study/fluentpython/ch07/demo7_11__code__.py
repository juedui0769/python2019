# 7-11
from fluentpython.ch07.demo7_9__average import make_average
if __name__ == '__main__':
    avg = make_average()
    _obj = avg.__code__.co_varnames
    print(_obj)
    _obj = avg.__code__.co_freevars
    print(_obj)