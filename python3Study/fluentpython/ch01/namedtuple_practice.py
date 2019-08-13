from collections import namedtuple

# namedtuple_practice.py
# import * from collections


def hello():
    """
    namedtuple: Return a new subclass of tuple with named fields.
    """
    Point = namedtuple('Point', ['x', 'y'])
    print(Point.__doc__) # docstring for the new class
    p = Point(11, y=22) # instantiate with positional args or keywords
    print(p[0]+p[1]) # indexable like a plain tuple
    x, y = p # unpack like a regular tuple
    print(x,y)
    print(p.x + p.y) # fields also accessible by name
    d = p._asdict() # convert to a dictionary
    print(d['x'])
    p1 = Point(**d) # convert from a dictionary
    print(p1)
    p2 = p._replace(x=100) # _replace() is like str.replace() but targets named fields
    print(p2)

# 这个方法证明`namedtuple`是可以提供大于`2`的字段的。
def hello2():
    Student = namedtuple('Student', ['id', 'name', 'age'])
    print(Student.__doc__)
    print(Student.__name__)
    s1 = Student(1, 'xiaoming', 22)
    s2 = Student(1, 'xiaohong', 33)
    print(s1)
    print(s2)

if __name__ == '__main__':
    # hello()
    hello2()
