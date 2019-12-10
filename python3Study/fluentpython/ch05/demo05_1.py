
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

def test01():
    print(factorial(42))
    print(factorial.__doc__)
    print(type(factorial))

def main():
    test01()

if __name__ == '__main__':
    main()