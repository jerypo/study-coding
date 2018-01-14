# 1) 사용자로부터 몇단을 출력할지 받을 것
# 2) 해당단을 곱하기 1에서 곱하기 9까지 실행할 것


# dan = int(input("몇 단을 출력하시겠습니까?"))
# for num in range(1, 10):
# print(" {} * {} = {} ".format(dan, num, dan * num))

dan = int(input("몇 단을 출력하시겠습니까?"))
if dan > 0 and dan < 10:
    for num in range(1, 10):
        print("{} * {} = {}".format(dan, num, dan * num))
else:
    print("1에서 9까지의 숫자를 입력해주세요.")
