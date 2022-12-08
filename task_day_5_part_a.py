
import re

with open('input_5a_real.txt') as f:
    lines =  f.readlines()


matrix = {}
iter = 0
for line in lines:
    line = line.rstrip()
    iter += 1
    if re.search(r'[0-9]+', line):
        break
    else:
        i = 0
        ind = 0
        while ind < len(line) - 1:
            if line[ind:ind+4] == '    ':
                i += 1
                ind += 4
                continue
            item = line[ind:ind+4]
            item = item.split('[')[1][:1]
            i += 1
            if i in matrix:
                matrix[i].insert(0, item)
            else:
                matrix[i] = [item]
            ind += 4


lines = lines[iter+1:]
print(lines)
print(matrix)

for line in lines:
    line = line.rstrip()
    how_many, come_from, go_to = [int(x) for x in re.findall(r'\d+', line)]
    for i in range(how_many):
        matrix[go_to].append(matrix[come_from].pop())
        print(matrix)

result = ''
for i in range(1, 11):
    if i in matrix:
        result += matrix[i][len(matrix[i])-1]

print(result)
