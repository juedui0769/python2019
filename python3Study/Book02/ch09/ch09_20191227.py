(1, 2) + (3, 4)
(1, 2) * 4
T = (1, 2, 3, 4)
T[0], T[1:3]
x = (40)
x
y = (40,)
y
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)
tmp.sort()
tmp
T = tuple(tmp)
T
T1 = ('cc', 'aa', 'dd', 'bb')
T
T1
sorted(T1)
T1
T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
L
T = (1, 2, 3, 2, 4, 2)
T.index(2)
T.index(2, 2)
T.count(2)
from collections import namedtuple
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])
bobo
bob
bob[0], bob[2]
bob.name, bob.jobs
O = bob._asdict()
O['name'], O['jobs']
O
bob = Rec('Bob', 40.5, ['dev', 'mgr'])
bob
name, age, jobs = bob
name, jobs
for x in bob: print(x)
bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
bob
job, name, age = bob.values()
name, job
for x in bob: print(bob[x])
for x in bob.values(): print(x)
%hist -f ch09_20191227.py
