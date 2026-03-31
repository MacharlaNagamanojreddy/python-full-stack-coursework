import random

def dice():
    return random.randint(1, 6)

def get_valid_input(player):
    while True:
        status = input(f"[Player {player}]: [P]lay or [Q]uit: ").lower()
        if status in ['p', 'q']:
            return status
        else:
            print("Invalid input. Enter only 'P' or 'Q'.")

player1_score, player2_score = 0, 0
winning_point = 100

ladders = {6:25, 12:31, 35:90, 46:60, 51:74, 78:99, 82:96}
snakes = {24:5, 45:18, 66:33, 74:37, 88:77, 93:57, 98:21}

turn = 1

while player1_score < winning_point and player2_score < winning_point:

    if turn == 1:
        status = get_valid_input(1)

        if status == 'q':
            print("Player 1 Quit!")
            break

        dice_val = dice()
        print(f'Dice: {dice_val}')

        if player1_score + dice_val <= winning_point:
            player1_score += dice_val

            if player1_score in ladders:
                player1_score = ladders[player1_score]
                print(f'Ladder to {player1_score}')

            elif player1_score in snakes:
                player1_score = snakes[player1_score]
                print(f'Snake to {player1_score}')
        else:
            print("Move not allowed")

        print(f'Player 1 Score: {player1_score}')
        turn = 2

    else:
        status = get_valid_input(2)

        if status == 'q':
            print("Player 2 Quit!")
            break

        dice_val = dice()
        print(f'Dice: {dice_val}')

        if player2_score + dice_val <= winning_point:
            player2_score += dice_val

            if player2_score in ladders:
                player2_score = ladders[player2_score]
                print(f'Ladder to {player2_score}')

            elif player2_score in snakes:
                player2_score = snakes[player2_score]
                print(f'Snake to {player2_score}')
        else:
            print("Move not allowed")

        print(f'Player 2 Score: {player2_score}')
        turn = 1

if player1_score >= winning_point:
    print("Player 1 Wins")
elif player2_score >= winning_point:
    print("Player 2 Wins")
else:
    print("Game Ended")