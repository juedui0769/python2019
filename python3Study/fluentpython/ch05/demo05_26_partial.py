# 示例5-26
from operator import mul
from functools import partial
def main():
    triple = partial(mul, 3) #(1)
    _obj = triple(7) #(2)
    print(_obj)
    _obj = list(map(triple, range(1, 10))) #(3)
    print(_obj)
if __name__ == '__main__':
    main()