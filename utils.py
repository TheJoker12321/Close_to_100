import random

def roll_two_d6() -> tuple[int, int]:
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    return roll_1 , roll_2

def is_bust(score: int) -> bool:
    return score > 100

def is_exact_100(score: int) -> bool:
    return score == 100

def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    player_1 = target - a
    player_2 = target - b
    if player_1 > player_2:
        return 2
    elif player_2 > player_1:
        return 1
    else:
        return None

def tie_breaker() -> int:
    while True:
        player1 = roll_two_d6()
        player2 = roll_two_d6()
        if player1 != player2:
            break
    if player1 > player2:
        return 1
    return 2


def turn_decision() -> str:
    choose = input("choose r for roll or p for pass: ")
    while choose != "r" and choose != "p":
        print("try again")
        choose = input("choose r for roll or p for pass: ")
    return choose

