import random

inventory = []

def game_over():
    print("게임오버. 다시 한번 모험을 시작하시겠습니까?")
    choice = input("'네' 혹은 '아니요'를 입력해주세요: ")
    if choice.lower() == '네':
        print("게임을 재시작 합니다")
        init_game()
    elif choice.lower() == '아니요':
        print("게임을 플레이해주셔서 감사합니다")
        exit()
    else:
        game_over()


def game_clear():
    print("당신은 드래곤을 물리치고 게임을 클리어하였습니다")


def fight_dragon():
    print("당신은 드래곤에게 다가갑니다")
    print("당신은 드래곤을 공격헙니다")
    damage = random.randint(1, 100)
    print(f"당신은 드래곤에게 {damage}의 데미지를 입혔습니다")
    if damage >= 50:
        print("당신은 드래곤을 처치하였습니다")
        game_clear()
    else:
        print("당신은 드래곤에게 패배하였습니다")
        game_over()

def cave_path():
    print("당신은 동굴 깊숙히 들어가다 커다란 드래곤이 잚들어 있는것을 발견합니다")
    print("용과의 싸움을 하시기 위해서 '공격'을 입력해주세요. 도망치고 싶으시다면 '도망'을 입력해주세요. 강으로 가고 싶으시면 'river'를 입력하세요")
    choice = input("당신의 선택: ")
    if choice.lower() == '공격':
        if '검' in inventory:
            fight_dragon()
        else:
            print("당신은 검을 가지고 있지 않습니다, 검을 획득하기 위해서 강으로 이동하세요")
            cave_path()
    elif choice.lower() == '강':
        print("당신은 강으로 이동합니다")
        river_path()
    elif choice.lower() == '도망':
        print("당신은 도망칩니다")
        game_over()
    else:
        print("옳바르지 않은 입력어")
        cave_path()

def river_path():
    print("당신은 강을 따라 걷다가 반짝이는 검을 발견했습니다")
    print("반짝이는 것을 주으시길 원하시면 '검'라고 입력해주세요. 떠나시고 싶으시면 'leave'를 입력하세요")
    choice = input("당신의 선택은?: ")
    if choice.lower() == "검":
        if "검" not in inventory:
            inventory.append('검')
            print("당신은 검을 획득했습니다")
        else:
            print("당신은 이미 검을 소지중입니다")
    elif choice.lower() == '떠난다':
        print("당신은 검을 두고 갑니다")
    else:
        print("불가능한 선택지입니다, 재입력해주세요")
        river_path()
    print("당신은 동굴로 들어갑니다")
    cave_path() 


def init_game():
    print("welcome to the adventure game")
    print("당신은 현재 어두운 숲에 있습니다. 당신 앞에는 두 가지의 길이 있습니다")
    print("동굴로 들어가는 첫 번쨰길을 선택하고 싶으시면 '동굴'라고 입력해주세요. 강으로 가고싶으시면 '강'을 입력해주세요")
    choice = input("당신의 선택은?: ")
    if choice.lower() == '동굴':
        cave_path()
    if choice.lower() == '강':
        river_path()
    else:
        print("그 길로는 갈 수 없습니다")
        init_game()

init_game()