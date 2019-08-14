
def simple_coroutine(): #(1)
    print('-> coroutine started')
    # print('11')
    x = yield #(2)
    print('-> coroutine received:', x)

my_coro = simple_coroutine()
print(my_coro)
next(my_coro)
# next(my_coro)
my_coro.send(42)
