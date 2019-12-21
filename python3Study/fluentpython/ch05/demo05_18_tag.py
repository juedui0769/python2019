from fluentpython.ch05.ch05_tag import tag
import inspect


def main():
    sig = inspect.signature(tag) #(1)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    bound_args = sig.bind(**my_tag) #(2)
    print(bound_args)
    for name, value in bound_args.arguments.items(): #(4)
        print(name, '=', value)
    del my_tag['name'] #(5)
    # 下面语句会报错：  TypeError: missing a required argument: 'name'
    bound_args = sig.bind(**my_tag) #(6)
    print(bound_args)


if __name__ == '__main__':
    main()