class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def get(self):
        return self.x, self.y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def __str__(self):
        return "<{},{}>".format(self.x, self.y)

    def __eq__(self, other):
        # if self.x == other.x and self.y == other.y:
        #     return True
        # else:
        #     return False
        return self.x == other.x and self.y == other.y


v1 = Vector2d(1, 2)
v2 = Vector2d(1, 2)
v3 = Vector2d(1, 2)

v1.setx(10)
v1.sety(20)

print(v1.get())
print(v1)
print(v2 == v1)
print(v2 == v3)



