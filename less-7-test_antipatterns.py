# Broken atomicity
import time


def test_add_smth():
    user = create_new_user(email='some@ema.il')
    user.register()
    user.auth()
    smth = user.create_smth()
    smth.add()
    check(user.is_authorized())
    check(smth.is_added())
    check('some@ema.il' == user.email)


# Liar
def test_some_feature(self):
    do_smth()
    self.assertTrue(True)


# Giant не стоит наваливать все в одну кучу

# The secret Catcher
def test_smth_one_two_three(self):
    do_smth1()
    do_smth2()
    do_smth3()


# The Inspector
def test_obj(self):
    # _
    self.assertTrue(42, test_obj._answer)


# The Slowpoke

def test_pokemon(self):
    do_smth1()
    time.sleep(N)
    self.assertSmth()

# Summary
# * write tests
# not to many
# integration mostly
