# 실습 1
def return_my_name():
    return "상묵"


def repeat_my_name(n):
    for _ in range(n):
        print("상묵")


# 매개변수의 수가 정해져 있지 않을 때
print("ABC", 1, 1233, "aaa")

def my_sum(*args):
    return sum(args)

my_sum(1, 2, 3, 4, 5)

def sample(a, b, *args):
    print(a)
    print(b)
    print(args)

sample(1, 2, 3, 4, 5)

# 실습
def my_average(*args):
    total = 0
    length = 0

    for num in args:
        total += num
        length += 1

    return total / length

def my_average_ver_2(*args):
    return sum(args) / len(args)

def my_concat(ch, *args):
    return ch.join(args)

def my_concat_ver2(*args):
    lst = [x for x in args]
    ch = lst.pop(0)
    return ch.join(lst)

print(my_average(1, 2, 3, 4, 5) )
print(my_concat(",", "A", "B", "C"))

print(my_concat_ver2(",", "A", "B", "C"))

# 여러 개의 값을 출력
def sum_sub(a, b):
    return a + b, a - b

print(sum_sub(1, 2))
print(sum_sub(1, 2)[0])
print(sum_sub(1, 2)[1])

def sum_sub_ver2(a, b):
    return a + b
    return a - b
print(sum_sub_ver2(1, 2))


# 실습
def get_max_min(lst):
    if len(lst) < 2:
        return
    return max(lst), min(lst)

print(get_max_min([1, 2, 3, 4, 5, 6]))
print(get_max_min([1]))

# 매개변수 초기 설정
def login(email, password, remember_me=False):
    print("email:", email)
    print("password:", password)

    if remember_me:
        print("기억합니다!")


login("sangmook.kim@kaist.ac.kr", 1234)
login("sangmook.kim@kaist.ac.kr", 1234, True)

n = 1

def make_ten():
    global n
    n = 10

make_ten()

print("n:", n)


class Student:
    grade = 100
    cnt_love = 3
    name = "김영희"
    major = "Computer Science"

    def study(self):
        print("공부!!!!!!")

    def love(self, lover):
        print("I love ", lover)

    def work(self):
        print("알바알바!!!!")

    def print(self, alcohol):
        print("마시자!!!", alcohol)


class Computer:
    CPU = "인텔"
    main_memory = "16G"

    def cal(self):
        print("계산계산!!")


class Nationality:
    name = "Korea"

    def diplomacy(self, other):
        print("외교", other)

Nationality()














