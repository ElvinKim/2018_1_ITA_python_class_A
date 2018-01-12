class Knight:
    level = 20
    name = "만년동 꿀주먹"
    hp = 200

    def move(self, direction):
        print(direction + "방향으로 이동합니다.")

    def attack(self):
        print(self)
        print(self.name + "이(가) 공격합니다.")


knight1 = Knight()
knight2 = Knight()

print(knight1.name, knight1.hp)
knight1.attack()
print(knight1)

print("-" * 20)
##########################################3
print(Knight.__dict__)
print(knight1.__dict__)

knight1.level = 30
print(knight1.__dict__)
print(knight1.level)

print("-" * 20)
##########################################3
knight1.name = "만년동 핵주먹"
knight1.hp = "40"

knight2.name = "몰라몰라"
knight2.level = 50


class Wizard:
    level = 1000

    def __init__(self, n, h, l=1):
        self.level = l
        self.name = n
        self.hp = h

    def move(self, direction):
        print(direction + "방향으로 이동합니다.")

    def attack(self):
        print(self.name + "이(가) 공격합니다.")

    def magic(self):
        print(self.name + "이(가) 마법을 사용합니다.")

    def get_level(self):
        return self.level

    def set_level(self, level):
        if level > 999:
            level = 999
        self.level = level


wizard1 = Wizard("어은동 핵폭탄", 600, 1)
wizard2 = Wizard("궁동 핵폭탄", 300, 100)

print(wizard1.name, wizard1.level, wizard1.hp)

print(wizard1.level)
print(Wizard.level)
print(Wizard.__dict__)
print("-" * 20)
##########################################

# 객체변수 변경
print(wizard1.get_level())
print(wizard1.level)

wizard1.set_level(100000)
print(wizard1.get_level())


class Student:
    def __init__(self, name, major, grade):
        self.name = name
        self.major = major
        self.grade = grade

    def study(self):
        print(self.name + "이(가) 공부!!!!!!")

    def love(self, lover):
        print("I love ", lover)

    def work(self):
        print("알바알바!!!!")

    def drink(self, alcohol):
        print("마시자!!!", alcohol)


s1 = Student("김영희", "컴퓨터 공학", 390)
s2 = Student("유재석", "뇌공학", 398)
s2.study()
s1.drink("백세주")


class Character:
    def __init__(self, n, h, l=1):
        self.level = l
        self.name = n
        self.hp = h

    def move(self, direction):
        print(direction + "방향으로 이동합니다.")

    def attack(self):
        print(self.name + "이(가) 공격합니다.")

    def get_level(self):
        return self.level

    def set_level(self, level):
        if level > 999:
            level = 999
        self.level = level


class Knight(Character):
    pass


class Archer(Character):
    pass


class Wizard(Character):
    def magic(self):
        print(self.name + "이(가) 마법을 사용합니다.")
