import json
from django.test import TestCase
from django.urls import reverse


def square_root_bi(x, epsilon):
    """Return y s.t. y*y is within epsilon of x"""
    assert x >= 0, 'x must be a non-negative, not ' + str(x)
    assert epsilon > 0, 'epsilon must be a positive, not' + str(epsilon)
    low = 0
    high = max(x, 1.0)
    guess = (low + high) / 2.0
    ctr = 1
    max_ctr = 1000
    while abs(guess**2 - x) > epsilon and ctr <= max_ctr:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        ctr += 1
    assert ctr <= max_ctr, 'Iteration count exceeded'
    print('Bi method. Num. iterations:', ctr, 'Estimate:', guess)
    return guess


def score2mark(score):
    if 0 <= score <= 59:
        return 2
    elif 60 <= score <= 74:
        return 3
    elif 75 <= score <= 89:
        return 4
    elif 90 <= score <= 100:
        return 5
    raise ValueError("Invalid score %s" % score)


# square_root_bi(0.25, 0.001)

def test_bi():
    print("square_root_bi(4, 0.0001)")
    square_root_bi(4, 0.0001)

    print("square_root_bi(9, 0.0001)")
    square_root_bi(9, 0.0001)

    print("square_root_bi(2, 0.0001)")
    square_root_bi(2, 0.0001)

    print("square_root_bi(.25, 0.0001)")
    square_root_bi(.25, 0.0001)

# test_bi()


# print(score2mark(70))
def test_mark_valid_score():
    score_to_expected_mark = {
        40: 2,
        65: 3,
        80: 4,
        95: 5,
    }
    for s, m in score_to_expected_mark.items():
        returned_mark = score2mark(s)
        assert returned_mark == m, 'Mark for score %s is %s, but %s expected' % (s, returned_mark, m)


test_mark_valid_score()


def test_mark_invalid_score():
    for s in (-1, 101, 2**64, ""):
        try:
            m = score2mark(s)
        except Exception as e:
            assert isinstance(e, ValueError), "Unexpected error: %s: %s" % (type(e), e)
        else:
            raise AssertionError("No error for bad value: score2mark(%s) -> %s") % (s, m)


def test_mark_float_score():
    s = 3.14
    expected_mark = 2
    m = score2mark(s)
    assert m == expected_mark, "Mark for score %s is %s, but %s expected" % (s, m, expected_mark)


# test_mark_invalid_score()
# test_mark_float_score()

class AccountApiTestCase(TestCase):
    def setUp(self):
        super(AccountApiTestCase, self).setUp()
        self.user.access_api_v2 = True
        self.user.save()

    def test_api_access(self):
        response = self.client.get(reverse('user-api'))
        self.assertEqual(response.status_code, OK)

        self.user.access_api_v2 = False
        self.user.save()
        response = self.client.get(reverse('user-api'))
        self.assertEqual(response.status_code, FORBIDDEN)

    def test_create_token(self):
        self.make_user_not_admin(self.user)
        # При первом заходе генерируется ключ доступа
        self.client.get(reverse('user-api'))
        api_key = ApiKey.objects.get(user=self.user, is_blocket=False)
        self.assertEqual(api_key.allowed_ips, [])
        self.assertEqual(api_key.expired, None)

        # При втором заходе уже не генерируется
        self.client.get(reverse('user-api'))
        self.assertEqual(ApiKey.objects.filter(user=self.user).count(), 1)

