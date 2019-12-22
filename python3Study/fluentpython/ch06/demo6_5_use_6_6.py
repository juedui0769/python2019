# 示例6-5
from fluentpython.ch06.demo6_6_best_promo import *
def main():
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermello', 5, 5.0)]
    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    long_order = [LineItem(str(item_code), 1, 1.0)
                  for item_code in range(10)]

    _obj = Order(joe, long_order, best_promo) #(1)
    print(_obj)
    _obj = Order(joe, banana_cart, best_promo) #(2)
    print(_obj)
    _obj = Order(ann, cart, best_promo) #(3)
    print(_obj)
if __name__ == '__main__':
    main()