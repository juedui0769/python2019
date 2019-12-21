from functools import reduce
# 示例5-21 使用 reduce 函数和一个匿名函数计算阶乘
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))
