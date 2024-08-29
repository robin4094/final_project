def cave_path():
    print("당신은 동굴 깊숙히 들어가다 커다란 용이 잚들어 있는것을 발견합니다")
    print("용과의 싸움을 하시기 위해서 'attack'을 입력해주세요. 도망치고 싶으시다면 'run'을 입력해주세요")

if choice.lower =='fight'


def river_path():
    print("당신은 강을 따라 걷다가 반짝이는 검을 발견했습니다")
    print("반짝이는 것을 주으시길 원하시면 'sword'라고 입력해주세요. 떠나시고 싶으시면 'leave'를 입력하세요")

    choice = input("당신의 선택은?: ")


if choice.lower() == 'sword':
    if sword not in inventory:
        inventory.append('sword')
        print("당신은 검을 획득했습니다")
    else:
        print("당신은 이미 검을 소지중입니다")
    elif choice.lower() == 'leave':
        print("당신은 검을 두고 갑니다")
    else:
        print("불가능한 선택지입니다, 재입력해주세요")
def init_game():
    print("welcome to the adventure game")
    print("당신은 현재 어두운 숲에 있습니다. 당신 앞에는 두 가지의 길이 있습니다")
    print("동굴로 들어가는 첫 번쨰길을 선택하고 싶으시면 'cave'라고 입력해주세요. 강으로 가고싶으시면 'river'를 입력해주세요")
    choice = input("당신의 선택은?: ")
    if choice.lower() == 'cave':
        cave_path()
    if choice.lower() == 'river':
        river_path()
    else:
        print("그 길로는 갈 수 없습니다")
        init_game()

init_game()