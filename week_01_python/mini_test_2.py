# 미니과제2 학교 클래스 만들기
# 이름, 설립연도, 주소


class School:
    def __init__(self, name, yymm, address):
        self.name = name
        self.yymm = yymm
        self.address = address

School1 = School("서울대학교", "1987년", "서울")
School2 = School("하버드", "1988년", "미국")
School3 = School("북경대학교", "1989년", "중국")

print(School1.name)
print(School2.yymm)
print(School3.address)
