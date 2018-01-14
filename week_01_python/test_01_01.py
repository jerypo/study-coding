# 맛집 고르기
import random

list_kr =["김치찌개", "된장찌개", "비빔밥", "육개장"]
list_jp =["초밥", "우동", "라면"]
list_ch = ["짜장면", "탕수육", "북경오리"]
menu_choice=input("한식, 중식, 일식 중 어떤 종류의 음식을 원하세요?")

# print(random.choice(list_kr))

# if menu_choice == "한식":
#     print("오늘저녁은 " + random.choice(list_kr) + "어떠신가요?")
# elif menu_choice == "중식":
#     print("오늘저녁은 " + random.choice(list_ch) + "어떠신가요?")
# elif menu_choice == "일식":
#         print("오늘저녁은 " + random.choice(list_jp) + "어떠신가요?")
# else:
#     print("한식, 중식, 일식 중 골라주세요.^^")

if menu_choice == "한식":
    menu_result = random.choice(list_kr)
    # menu_result = list_kr(random.randint(0, len(list_kr)))
elif menu_choice == "중식":
    menu_result = random.choice(list_ch)
elif menu_choice == "일식":
    menu_result = random.choice(list_jp)
else:
    print("한식, 일식, 중식 중에서 선택해주세요")
if menu_result:
    print("{} 중에서 {}가 선택되었습니다.".format(menu_choice, menu_result))
