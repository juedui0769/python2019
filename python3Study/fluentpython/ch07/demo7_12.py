
from fluentpython.ch07.demo7_9__average import make_average
if __name__ == '__main__':
    avg = make_average()
    avg(10)
    avg(11)
    avg(12)
    _obj = avg.__code__.co_freevars
    print(_obj)
    _obj = avg.__closure__
    print(_obj)
    _obj = avg.__closure__[0].cell_contents
    print(_obj)