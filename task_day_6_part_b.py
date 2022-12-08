with open('input_6a_real.txt') as f:
    line = f.readline()

index = 0
while index + 14 < len(line):
    to_check = line[index:index+14]
    if len(set(to_check)) == 14:
        print(to_check, index + 14)
        break
    index += 1

