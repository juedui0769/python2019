# 示例6-7
from fluentpython.ch06.demo6_3_Order import *

promos = [globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promo']

def best_promo(order):
    return max(promo(order) for promo in promos)

def _test():
    # _obj = globals()
    # print(_obj)
    _list = [name for name in globals()
             if name.endswith('_promo')
             and name != 'best_promo']
    print(_list)
    # import fluentpython.ch06.demo6_3_Order as demo
    # # 下面代码会报错
    # _obj = demo.globals()
    # print(_obj)
if __name__ == '__main__':
    _test()