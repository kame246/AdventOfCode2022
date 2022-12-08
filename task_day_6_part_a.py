with open('input_6a_real.txt') as f:
    line = f.readline()

index = 0
length = 4 # 14 for second part
while index + length < len(line):
    to_check = line[index:index+length]
    if len(set(to_check)) == length:
        print(to_check, index + length)
        break
    index += 1

