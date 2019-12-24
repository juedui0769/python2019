# 7-10
from fluentpython.ch07.demo7_9__average import make_average
if __name__ == '__main__':
    avg = make_average()
    _avg = avg(10)
    print(_avg)
    _avg = avg(11)
    print(_avg)
    _avg = avg(12)
    print(_avg)