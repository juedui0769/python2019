# 7-5

b = 6
def f2(a):
    print(a)
    # UnboundLocalError: local variable 'b' referenced before assignment
    print(b)
    b = 9

f2(3)