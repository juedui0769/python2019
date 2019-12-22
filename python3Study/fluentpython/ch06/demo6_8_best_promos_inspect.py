# 示例6-8
import fluentpython.ch06.promotions as promotions
import inspect

promos = [func for name, func in
          inspect.getmembers(promotions, inspect.isfunction)]

def best_promo(order):
    return max(promo(order) for promo in promos)

if __name__ == '__main__':
    print(promos)