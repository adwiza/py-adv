
class Enemy:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def getvars(self):
        one = self.one
        two = self.two
        print(two)


enemy = Enemy(69, 49)

enemy.getvars()
