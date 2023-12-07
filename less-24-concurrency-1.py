"""import_mock.py"""

to_mock = None

import import_mock
from multiprocessing import Process


class A(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def __getstate__(self):
        print('__getstate__')
        return {'a': self.a, 'b': self.b, 'c': 0}


def func():
    import_mock.to_mock = 1
    a = A()
    return a


def func1(a):
    print(a.a, a.b, a.c)
    print(import_mock.to_mock)


if __name__ == '__main__':
    a = func()
    p = Process(target=func1, args=(a,))
    p.start()
    p.join()