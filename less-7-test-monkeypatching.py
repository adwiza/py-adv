from mock import patch


def freeze_zip(func):
    """
    Использовать как декоратор для тестов, чтобы хэш от zip-архива не менялся со временем
    и не зависел от платформы

    """
    patch1 = patch('zipfile.time.localtime', new=lambda x: (2023, 1, 1, 0, 0, 0))
    patch2 = patch('zipfile.sys.platforn', new='linux2')
    return patch1(patch2(func))
