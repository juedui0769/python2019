# 示例6-2
# import fluentpython.ch06.demo6_1 as demo
from fluentpython.ch06.demo6_1 import Customer
from fluentpython.ch06.demo6_1 import LineItem
from fluentpython.ch06.demo6_1 import Order
from fluentpython.ch06.demo6_1 import Promotion, FidelityPromo
from fluentpython.ch06.demo6_1 import BulkItemPromo, LargeOrderPromo

def main():
    joe = Customer('John Doe', 0) #(1)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermello', 5, 5.0)] #(2)
    _obj = Order(joe, cart, FidelityPromo()) #(3)
    print(_obj)
    _obj = Order(ann, cart, FidelityPromo()) #(4)
    print(_obj)
    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)] #(5)
    _obj = Order(joe, banana_cart, BulkItemPromo()) #(6)
    print(_obj)
    long_order = [LineItem(str(item_code), 1, 1.0)
                  for item_code in range(10)] #(7)
    _obj = Order(joe, long_order, LargeOrderPromo()) #(8)
    print(_obj)
    _obj = Order(joe, cart, LargeOrderPromo())
    print(_obj)

if __name__ == '__main__':
    main()