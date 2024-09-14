# import numpy as np
# import random
#
#
# def check_result(total_pc_player, character):
#     global in_round
#     # TODO check if out out slot
#     if len(moves) == 9:
#         print(f'Draw!\nCurrent score: player - {player_score} | pc - {pc_score}\nAnother round!')
#         in_round = False
#     # TODO check if column has 3 same values
#     col_list = [table[:, i] for i in range(0, 2)]
#     for c in col_list:
#         for c_value in c:
#             if c_value == character:
#                 total_pc_player += 1
#         if total_pc_player == 3:
#             in_round = False
#         total_pc_player = 0
#     # TODO check if row has 3 same values
#     row_list = [table[i] for i in range(0, 2)]
#     for r in row_list:
#         for r_value in r:
#             if r_value == character:
#                 total_pc_player += 1
#         if total_pc_player == 3:
#             in_round = False
#         total_pc_player = 0
#     # TODO check if diagonal has 3 same values
#     diagonal = np.diag(table)
#     anti_diagonal = np.diag(table[::-1])
#     for d in diagonal:
#         if d == character:
#             total_pc_player += 1
#     if total_pc_player == 3:
#         in_round = False
#     else:
#         total_pc_player = 0
#     for ad in anti_diagonal:
#         if ad == character:
#             total_pc_player += 1
#     if total_pc_player == 3:
#         in_round = False
#
#
# def player_turn(character_player):
#     while True:
#         player_first_input_row = int(input('Your turn, input row index: '))
#         player_first_input_column = int(input('Now, input column index: '))
#         if [player_first_input_row, player_first_input_column] not in moves:
#             break
#         else:
#             print("Slot's already taken")
#     moves.append([player_first_input_row, player_first_input_column])
#     table[player_first_input_row, player_first_input_column] = character_player
#     check_result(total_player, character_player)
#
#
# def pc_turn(character_player):
#     while True:
#         pc_turn_row = random.randint(0, 2)
#         pc_turn_column = random.randint(0, 2)
#         if [pc_turn_row, pc_turn_column] not in moves:
#             break
#     moves.append([pc_turn_row, pc_turn_column])
#     print('PC turn')
#     table[pc_turn_row, pc_turn_column] = character_player
#     print(table)
#     check_result(total_pc, character_player)
#
#
# def start_turn(random_number):
#     global player_score, pc_score
#     while True:
#         if in_round:
#             if random_number == 0:
#                 player_turn('X')
#             else:
#                 pc_turn('X')
#         else:
#             if random_number == 0:
#                 player_score += 1
#             else:
#                 pc_score += 1
#             print(f'Current score: player - {player_score} | pc - {pc_score}\nAnother round!')
#             break
#         if in_round:
#             if random_number == 1:
#                 player_turn('O')
#             else:
#                 pc_turn('O')
#         else:
#             if random_number == 1:
#                 player_score += 1
#             else:
#                 pc_score += 1
#             print(f'Current score: player - {player_score} | pc - {pc_score}\nAnother round!')
#             break
#
#
# # TODO main game
# is_game = True
#
# while is_game:
#     table = np.zeros((3, 3), dtype=str)
#     in_round = True
#     total_player = 0
#     total_pc = 0
#     player_score = 0
#     pc_score = 0
#     moves = []
#     first_turn = random.randint(0, 1)
#     print(first_turn)
#     if first_turn == 0:
#         print("Player moves first\n")
#         print(table)
#         start_turn(first_turn)
#     else:
#         print("PC moves first\n")
#         start_turn(first_turn)
import numpy as np
import random

def check_result(table):
    for player in ['X', 'O']:
        # Check columns
        for col in range(3):
            if all(table[row, col] == player for row in range(3)):
                return player

        # Check rows
        for row in range(3):
            if all(table[row, col] == player for col in range(3)):
                return player

        # Check diagonals
        if all(table[i, i] == player for i in range(3)):
            return player
        if all(table[i, 2 - i] == player for i in range(3)):
            return player

    # Check for draw
    if np.all(table != ' '):
        return 'Draw'

    return None

def player_turn(table, character):
    while True:
        player_first_input_row = int(input('Your turn, input row index: '))
        player_first_input_column = int(input('Now, input column index: '))
        if 0 <= player_first_input_row < 3 and 0 <= player_first_input_column < 3 and table[player_first_input_row, player_first_input_column] == ' ':
            break
        else:
            print("Invalid input or slot is already taken")
    table[player_first_input_row, player_first_input_column] = character

def pc_turn(table, character):
    while True:
        pc_turn_row = random.randint(0, 2)
        pc_turn_column = random.randint(0, 2)
        if table[pc_turn_row, pc_turn_column] == ' ':
            break
    table[pc_turn_row, pc_turn_column] = character

def start_game():
    player_score = 0
    pc_score = 0

    while True:
        table = np.full((3, 3), ' ')
        moves = []

        first_turn = random.randint(0, 1)
        if first_turn == 0:
            print("Player moves first\n")
        else:
            print("PC moves first\n")

        while True:
            print(table)
            if first_turn == 0:
                player_turn(table, 'X')
            else:
                pc_turn(table, 'O')

            result = check_result(table)
            if result:
                print(table)
                if result == 'X':
                    player_score += 1
                elif result == 'O':
                    pc_score += 1
                print(f"Result: {result}")
                print(f"Current score: Player - {player_score} | PC - {pc_score}")
                break

            first_turn = 1 - first_turn

        play_again = input("Play another round? (y/n): ")
        if play_again.lower() != 'y':
            break

start_game()
