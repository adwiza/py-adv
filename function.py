def square(value):
    return value ** 2


def cube(value):
    return value ** 3


def main(value):
    return square(value) + cube(value)


if __name__ == '__main__':
    main(value=1)
