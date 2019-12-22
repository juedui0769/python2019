# 示例6-4
from fluentpython.ch06.demo6_3_Order import *
def main():
    joe = Customer('John Doe', 0) #(1)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermello', 5, 5.0)]
    _obj = Order(joe, cart, fidelity_promo) #(2)
    print(_obj)
    _obj = Order(ann, cart, fidelity_promo)
    print(_obj)
    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    _obj = Order(joe, banana_cart, bulk_item_promo) #(3)
    print(_obj)
    long_order = [LineItem(str(item_code), 1, 1.0)
                  for item_code in range(10)]
    _obj = Order(joe, long_order, large_order_promo)
    print(_obj)
    _obj = Order(joe, cart, large_order_promo)
    print(_obj)
if __name__ == '__main__':
    main()