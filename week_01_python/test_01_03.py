# 가위 바위 보 게임
import  random
rock = "바위"
scissors = "가위"
paper = "보"

rsp_list = (
    rock,
    scissors,
    paper
)

win_count = 0
lose_count = 0

while win_count < 3 and lose_count < 3:
# 1) 사용자 입력
    user_choice = input("{}, {}, {}: ".format(rock, scissors, paper))

# 2) 컴퓨터 임의 선택
    computer_choice = random.choice(rsp_list)
    if user_choice == computer_choice:
        print("비겼습니다.")
    elif user_choice not in rsp_list:
        print("가위, 바위, 보 중에서 하나를 입력해주세요.")
    elif ((user_choice == rock and computer_choice == scissors)
        or (user_choice == scissors and computer_choice == paper)
        or (user_choice == paper and computer_choice == rock)):
        win_count = win_count + 1
        print("이겼습니다.")
    else:
        lose_count = lose_count + 1
        print("가위, 바위, 보 중 선택하세요")
# 3) 3번 지거나 이기면 승패 확정
if win_count == 3:
    print("사용자가 최종 승리하였습니다.")
else:
    print("컴퓨터가 최종 승리하였습니다.")
