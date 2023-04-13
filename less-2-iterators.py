import gzip


class CompressedList(list):
    def __iter__(self):
        return CompressedListIterator(self)


class CompressedListIterator:
    def __init__(self, arr):
        self.arr = arr
        self.counter = 0
        self.index = 0

    def __next__(self):
        if self.index >= len(self.arr):
            raise StopIteration()
        if self.counter < self.arr[self.index][1]:
            self.counter += 1
            return self.arr[self.index][0]
        else:
            self.counter = 0
            self.index += 1
            return self.__next__()

    # Easy way
    # def __next__(self):
    #     for pair in self.arr:
    #         for x in range(pair[1]):
    #             yield pair[0]


# original = [1, 1, 1, 1, 2, 2, 1, 1, 1, 3, 3, 3, 3]
# compressed = CompressedList([(1, 4), (2, 2), (1, 3), (3, 4)])
# decompressed = [x for x in compressed]
# print(original)
# print(decompressed)
# print(original == decompressed)

def gen():
    yield 1
    yield 2
    yield 3
    prev = 0
    cur = 1
    while True:
        next_val = prev + cur
        yield next_val
        prev, cur = cur, next_val


# g1 = gen()
# g2 = gen()
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))


# read file
# def xreadlines(log_path):
#     if log_path.endswith('.gz'):
#         log = gzip.open(log_path, 'rb')
#     else:
#         log = open(log_path)
#     total = processed = 0
#     for line in log:
#         parsed_line = process_line(line)
#         total += 1
#         if parsed_line:
#             processed += 1
#             yield parsed_line
#     print('%s of %s lines processed' % (processed, total))
#     log.close()

[x * x for x in range(10)]
g = (x * x for x in range(1000000000000))


# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def pow_func(n):
    def f(x: float) -> float:
        """
        :param x:
        :return:
        """
        return x ** n

    return f


# a = pow_func(3)
# print(a(2))

def btc_price_fetcher_fabric(url_getter, fetcher, parser, getter):
    def btc_price_fetcher():
        url = 'url'
        return url


class Fetcher:
    def url_getter(self):
        pass

    def fetcher(self):
        pass

    def run(self):
        pass


def a(x: int) -> int:
    return x * x


result = map(a, [1, 2, 3, 4])

# print(list(result))
# print(dir(result))
#
#
# def map(f, d):
#     for x in d:
#         yield f(x)


import timeit

t1 = timeit.timeit(
    """list(filter(lambda x: x % 2 == 0, map(a, [1, 2, 3, 4])))""",
    globals=globals()
)

t2 = timeit.timeit(
    """result=[a(x) for x in [1, 2, 3, 4] if a(x) % 2 == 0]""",
    globals=globals()
)

# print(t1)
# print(t2)


# def fg():
#     d = {'cnt': 0}
#
#     def f():
#         d['cnt'] += 1
#         print(d)
#     return f

def fg():
    d = 0

    def f():
        nonlocal d
        d += 1
        print(d)

    return f


# q = fg()
# q()
# q()
# q()


def create_multipliers():
    return [lambda x, i_=i: i_ * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))
