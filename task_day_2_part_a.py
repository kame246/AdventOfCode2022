to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
points = {'X': 1, 'Y': 2, 'Z': 3}
to_opponent_choice = {'X': 'A', 'Y': 'B', 'Z': 'C'}

score = 0

with open('input_2a_real.txt') as f:
    for round_data in f.readlines():
        opponent_choice, my_choice = round_data.rstrip().split(' ')
        if opponent_choice == to_opponent_choice[my_choice]:
            score += 3
        elif to_win[opponent_choice] == my_choice:
            score += 6
        score += points[my_choice]

print(f'{score=}')