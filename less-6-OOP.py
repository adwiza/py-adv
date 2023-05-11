class C():
    pass


x = C()


# print(x.foo)


def lookup(obj, attr):
    obj_cls = obj.__class__
    if hasattr(obj_cls, attr):
        d = getattr(obj_cls, attr)
        desc_cls = d.__class__
        if hasattr(desc_cls, '__get__') and (hasattr(desc_cls, '__set__') or attr not in obj.__dict__):
            return desc_cls.__get__(d, obj_cls)
    return obj.__dict__[attr]


# print(lookup(x, 'foo'))

x = C()
x.foo = 23


def setup(obj, attr, val):
    obj_cls = obj.__class__
    if hasattr(obj_cls, attr):
        d = getattr(obj_cls, attr)
        desc_cls = d.__class__
        if hasattr(desc_cls, '__set__'):
            desc_cls.__set__(d, obj, val)
        return
    obj.__dict__[attr] = val


def adder(x, y): return x + y


add23 = adder.__get__(23)  # 23.adder
print(add23, adder)
print(add23, 100)

# Magic methods

# References

a = C()
print(a.__dict__)

from abc import ABCMeta, abstractmethod, abstractproperty

# Metaclasses

print(object.__class__)
print(type.__class__)
print(object.__name__)
print(type.__name__)
print(object.__bases__)
print(type.__bases__)

name = 'Aleksei'
bases = (object,)
class_attributes = {'cool': True}

cls = type(name, bases, class_attributes)

####
# class Aleksei(object):
#      cool = True
# cls = Aleksei

obj = cls()
print(cls, cls.__dict__, obj.__class__)


class MyMetaClass(type):
    def __new__(meta, name, bases, dct):
        print('------------------------')
        print('creating class', name)
        print(meta)
        print(bases)
        print(dct)
        return super(MyMetaClass, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('Initializing class', name)
        print(cls)
        print(bases)
        print(dct)
        super(MyMetaClass, cls).__init__(name, bases, dct)

    def __call__(self, *args, **kwargs):
        print('-----------------------------------')
        print('__call__ if %s' % cls)
        print('__call__ *args=%s, **kwargs=%s' % (args, kwargs))
        return super(MyMetaClass, cls).__call__(*args, **kwargs)


class MyClass(object, metaclass=MyMetaClass):

    def __init__(self, min_woos, silent=False):
        self.min_woos = min_woos

    def woo(self, n):
        if self.silent:
            return
        for _ in range(max(self.min_woos, n)):
            print('Woo!')

    started = True


# MyClass(-1, silent=False)

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst


# subclassing isa problem
class Foo(Singleton): pass


class Bar(Foo): pass


f = Foo()
b = Bar()
