
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

def reverse(word):
    return word[::-1]

def test01():
    print(reverse('testing'))
    print(sorted(fruits, key=reverse))

def main():
    test01()


if __name__ == '__main__':
    main()