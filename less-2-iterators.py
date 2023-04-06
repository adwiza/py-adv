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

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))