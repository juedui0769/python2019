
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

def test02():
    fact = factorial
    print(fact)
    print(fact(5))
    print(map(fact, range(11)))
    print(list(map(fact, range(11))))

def main():
    test02()

if __name__ == '__main__':
    main()