import string

score = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase
points = dict(zip(list(alphabet), range(1, 53)))

with open('input_3a_real.txt') as f:
    data = f.readlines()

line_no = 0
while line_no < len(data):
    first, second, third = [set(x.rstrip()) for x in data[line_no:line_no+3]]
    common = first & second & third
    score += points[common.pop()]
    line_no += 3

print(f'{score=}')