# 7-5

b = 6
def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(3)
print(b)
print('-'*20)
f3(3)
print('-'*20)
b = 30
print(b)