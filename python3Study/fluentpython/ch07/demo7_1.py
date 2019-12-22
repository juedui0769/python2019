# 示例7-1
def deco(func):
    def inner():
        print('running inner()')
    return inner #(1)

@deco
def target(): #(2)
    print('running target()')

if __name__ == '__main__':
    target() #(3)
    print(target) #(4)