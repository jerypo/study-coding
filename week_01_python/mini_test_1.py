# 리스트나 튜플에서 임의의 하나 값 뽑기

# 0이상 1미만의 숫자 중 아무 숫자나 하나 뽑아서 돌려줌
import random
print(random.random())

#주사위처럼 1에서 6까지의 정수 중 하나 뽑기
print(random.randrange(1,7))

# 순서형 자료를 뒤죽박죽으로 섞기
list_a = [1, 2, 3, 4, 5]
random.shuffle(list_a)
print(list_a)

# 임의의 값 하나 뽑기
print(random.choice(list_a))

print(random.randint(1, 6))
