# 다이아몬드 그리기

#1
#11
#111
#1111
#11111
# for a in range(1, 6):
#     print("1" * a)

#10000
#11000
#11100
#11110
#11111
# for a in range(1, 6):
#     print("1" * a + "0" * (5-a))


for a in range(1, 6):
    a = a - 3
    if a < 0:
        a = -a
    print("0" * a + "1" * (5 - a * 2) + "0" * a)
