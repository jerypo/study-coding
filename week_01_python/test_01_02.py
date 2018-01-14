# 회사 조직도 만들기
# 1) 사람클래스 - 이름, 나이, 성별
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender= gender

    def read(self):
        self.view_count = self.view_count + 1

# 2) 직장동료 클래스 - 이름, 나이, 성별 + 직급(대리)
class Colleague(Person):
    # position = "대리"
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender)
        self.position = position


# colleague = Colleague("김지현", 32, "Female")
# print(colleague.name)

colleague = Colleague("김지현", 32, "Female", "대리")
print(colleague.__dict__)
