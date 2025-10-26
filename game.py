from utils import *

score_player_1 = 0
score_player_2 = 0
def play_game():
    global score_player_1
    global score_player_2
    flag = True
    check_pass = 0
    while flag:
        score_1_equal_100 = is_exact_100(score_player_1)
        score_2_equal_100 = is_exact_100(score_player_2)
        score_1_over_100 = is_bust(score_player_1)
        score_2_over_100 = is_bust(score_player_2)
        if check_pass == 2:
            result = closer_to_target(score_player_1, score_player_2)
            if result != 1 and result != 2:
                result_again = tie_breaker()
                print(f"player {result_again} won!!")
                break
            print(f"player {result} won!!!")
            break
        # Checking if one of them has passed 100
        if score_1_over_100 or score_2_over_100:
            if score_1_over_100:
                print("player 1 lose!! and player 2 won")
            else:
                print("player 2 lose!! and player 1 won")
            break
        # # Check, both of them reached 100
        # if score_1_equal_100 and score_2_equal_100:
        #     status_win = tie_breaker()
        #     print(f"{status_win} won!!")
        #     flag = False
        # Checking if one of them reached exactly one hundred
        if score_1_equal_100 or score_2_equal_100:
            # Check, both of them reached 100
            if score_1_equal_100 and score_2_equal_100:
                status_win = tie_breaker()
                print(f"{status_win} won!!")
            if score_1_equal_100:
                print("player 1 won!!")
            else:
                print("player 2 won!!")
            flag = False
        print("turn player 1:")
        choose1 = turn_decision()
        # Starting the game execution and turns
        if choose1 == "r":
            if check_pass == 1:
                check_pass = 0
            score_player1 = roll_two_d6()
            print(score_player1)
            score_player_1 += score_player1[0]
            score_player_1 += score_player1[1]
            print(f"Your total score: {score_player_1} ")

        else:
            check_pass += 1
            print("turn player 2:")
            choose2 = turn_decision()
            if choose2 == "r":
                if check_pass == 1:
                    check_pass = 0
                score_player2 = roll_two_d6()
                print(score_player2)
                score_player_2 += score_player2[0]
                score_player_2 += score_player2[1]
                print(f"Your total score: {score_player_2}")
                continue
            else:
                check_pass += 1
                continue
        print("turn player 2:")
        choose2 = turn_decision()
        if choose2 == "r":
            if check_pass == 1:
                check_pass = 0
            score_player2 = roll_two_d6()
            print(score_player2)
            score_player_2 += score_player2[0]
            score_player_2 += score_player2[1]
            print(f"Your total score: {score_player_2}")
            continue
        else:
            check_pass += 1
            continue





