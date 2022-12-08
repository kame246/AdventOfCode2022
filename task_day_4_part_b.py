import string

score = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase
points = dict(zip(list(alphabet), range(1, 53)))

with open('input_3a_real.txt') as f:
    for racksack in f.readlines():
        racksack = racksack.rstrip()
        half = len(racksack) // 2
        first = racksack[:half]
        second = racksack[half:]
        common = set(first) & set(second)
        score += points[common.pop()]

print(f'{score=}')