def f():
    return 42


class SoleClass(object):
    classarrt = f()

    def method(self, arg):
        self.instanceattr = arg

    def helper(arg):
        return arg + 1

    for i in range(10):
        classarrt = helper(classarrt)
    del helper


print(SoleClass.__dict__)
print(dir(SoleClass()))


class C(object):
    def foo(self):
        pass


print(C.foo)
print(C.__dict__['foo'])
c = C()
print(c.__dict__)
print(c.foo)
print(c.foo(), C.foo(C))


class Classic:
    def method(cls):
        pass


print(Classic.__mro__)


class New(object):
    def method(self):
        pass


print(New.__mro__)

# MRO


class X(object): pass


class Y(object): pass
class A(X, Y): pass
class B(Y, X): pass


# class C(A, B): pass
# C3 Algorithm
print(B.__mro__)


class A(object):
    def __init__(self):
        print("I'm from A")

class B(A):
    def __init__(self):
        print("I'm from B")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print("I'm from C")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print("I'm from D")
        super(D, self).__init__()


d = D()

import collections
import logging

logging.basicConfig(level='INFO')


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info(f'Setting {key} to {value}')
        super(LoggingDict, self).__setitem__(key, value)


class LoggingOD(LoggingDict, collections.OrderedDict):
    # Build new functionality by reodering the MRO
    pass


ld = LoggingDict([('red', 1), ('green', 2), ('blue', 3)])
print(ld)
ld['red'] = 10

ld = LoggingDict([('red', 1), ('green', 2), ('blue', 3)])
print(ld)

ld['red'] = 10

class Root(object):
    def draw(self):
        assert not hasattr(super(Root, self), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super(Shape, self).__init__(**kwds)

    def draw(self):
        print('Drawing. Setting shape to:', self.shapename)
        super(Shape, self).draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing. Setting color to:', self.color)
        super(ColoredShape, self).draw()


cs = ColoredShape(color='blue', shapename='square')
cs.draw()


# Multiple inheritance

class SingleObjectMixin(ContexMixin):
    """
    Provides the ability to retrieve a single object for further manipulation.
    """
    model = None
    queryset = None
    slug_field = 'slug'
    contex_object_name = None
    slug_url_kwarg = 'pk'
    query_pk_and_slug = False

    # methods and stuff


class BaseDetailView(SingleObjectMixin, View):
    """
    A base view for displaying a single object
    """
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

# Fix class attributes
__slots__ = ['radius', 'pi']


class StandardClass(object):
    def __init__(self, x):
        self.x = x

newed_up_standard = object.__new__(StandardClass)
print(type(newed_up_standard) is StandardClass)
print(hasattr(newed_up_standard, 'x'))

StandardClass.__init__(newed_up_standard, 5)
print(newed_up_standard.x == 5)
#> True
#> False
#> True

def instanctiate(cls, *args, **kwargs):
    obj = cls.__new__(cls, *args, **kwargs):
    if instanctiate(obj, cls):
        cls.__init__(obj, *args, **kwargs)
    return obj

class Singleton(object):
    def __new__(cls, *a, **k):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *a, **k)



# Name mangling
# Double underscore (class local reference) is not for privacy. It's for referring to self.

# Introspection

import inspect
print(inspect(getmemers(object)))
