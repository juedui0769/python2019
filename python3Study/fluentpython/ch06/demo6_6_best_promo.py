# 示例6-6
from fluentpython.ch06.demo6_3_Order import *

promos = [fidelity_promo, bulk_item_promo, large_order_promo] #(1)

def best_promo(order): #(2)
    return max(promo(order) for promo in promos) #(3)