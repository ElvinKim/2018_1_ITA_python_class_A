while True:
    try:
        a = int(input("a="))
        b = int(input("b="))
        print(a/b)
    except TypeError as e:
        print(e)
        print("문자열을 문자열로 나눌 수 없다!!!")
    except ZeroDivisionError as e:
        print(e)
        print("0으로 나눌 수 없다!!!")


class Person:
    def introduce(self):
        raise NotImplemented


class Police(Person):
    def introduce(self):
        print("저는 경찰관입니다!!!")

kim = Police()
kim.introduce()


class ScoreError(Exception):
    def __str__(self):
        return "점수의 허용 범위를 넘었습니다."


score = 100

def input_score(s):
    if s < 0 or s >100:
        raise ScoreError()
    print(str(s) + "점을 입력합니다.")


#input_score(score)

try:
    input_score(101)
except ScoreError as e:
    print(e)





