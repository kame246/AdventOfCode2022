to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
to_loss = {'A': 'Z', 'B': 'X', 'C': 'Y'}
points = {'X': 1, 'Y': 2, 'Z': 3}
to_opponent_choice = {'X': 'A', 'Y': 'B', 'Z': 'C'}
to_my_choice = {'A': 'X', 'B': 'Y', 'C': 'Z'}

score = 0

with open('input_2a_real.txt') as f:
    for round_data in f.readlines():
        opponent_choice, should_be = round_data.rstrip().split(' ')
        if should_be == 'X': # loss
            my_choice = to_loss[opponent_choice]
            score += points[my_choice]
        elif should_be == 'Y': # draw
            my_choice = to_my_choice[opponent_choice]
            score += points[my_choice] + 3
        else: #win
            my_choice = to_win[opponent_choice]
            score += points[my_choice] + 6

print(f'{score=}')




# X for Rock 1,
#     Y for Paper 2,
#         and Z for Scissors 3



