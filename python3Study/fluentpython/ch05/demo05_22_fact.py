from functools import reduce
from operator import mul

# 示例5-22 使用 reduce 和 operator.mul 函数计算阶乘
def fact(n):
    return reduce(mul, range(1, n+1))