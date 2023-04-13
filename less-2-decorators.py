import functools


def decorator(func):
    def wrapper(*args, **kwargs):
        print("args: ", args, "kwargs: ", kwargs)
        func(*args, **kwargs)
    return wrapper


@decorator
def f(a, b, c, platypus='Why not?'):
    print(a, b, c, platypus)


# def f(a, b, c, platypus='Why not?'):
#     print(a, b, c, platypus)
# f = decorator(f)


f('Bill', "Linus", "Stieve", platypus='Homer!')

# Для чего использовать декораторы?
#  - для регистрации обработчика /var/www/users/get
#  - логирование
#  - аутентификация
#  - кеш

# @cache
# def f(url) -> str:
#     pass

from functools import wraps


class Deprecated(object):
    # def __init__(self):
    #     pass

    def __call__(self, func):
        self.func = func
        self.count = 0
        return self._wrapper

    def _wrapper(self, *args, **kwargs):
        self.count += 1
        if self.count == 1:
            print(self.func.__name__, "is deprecated")
        return self.func(*args, **kwargs)


@Deprecated()
def f():
    pass


print(f())
print(f())
print(f())





