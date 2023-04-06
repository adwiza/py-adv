def recv_count():
    try:
        while True:
            n = yield
            print('T-minus', n)
    except GeneratorExit:
        print('Boom!')


r = recv_count()
next(r)
for i in range(5, 0, -1):
    r.send(i)

r.close()
