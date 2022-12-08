with open('input_7a_temp.txt') as f:
    lines = f.readlines()

from pathlib import Path
pwd = Path('/')
disk = {}
num_line = 0
while num_line < len(lines):
    line = lines[num_line]
    if line.startswith('$'):
        line = line.rstrip()
        command, *params = line[2:].split(' ')
        print(command, params)
        if command == 'cd':
            if params[0] == '..':
                pwd = pwd.parent
            elif params[0].startswith('/'):
                pwd = Path(params[0])
            else:
                pwd = pwd / params[0]
            print(f'Changed dir to {pwd}')
        elif command == 'ls':
            while num_line < len(lines)-1 and not lines[num_line + 1].startswith('$'):
                num_line += 1
                line = lines[num_line].rstrip()
                a, b = line.split(' ')
                if a == 'dir':
                    dir_path = pwd / b
                    print(f'dir {dir_path}')
                    if pwd in disk:
                        disk[pwd].append(dir_path)
                    else:
                        disk[pwd] = [dir_path]
                else:
                    size = int(a)
                    file = b
                    if pwd in disk:
                        disk[pwd].append(size)
                    else:
                        disk[pwd] = [size]
                    print(f'size: {size} {file} {pwd}')
        num_line += 1

print(disk)

# for f in disk:
#     values = disk[f]
#     for v in values:

def calc_size(path):
    s = 0
    for f in disk[path]:
        if isinstance(f, int):
            s += f
        else:
            s += calc_size(f)
    return s

for path in disk:
    disk[path] = calc_size(path)

print(disk)

to_sum = [x for x in disk.values() if x <= 100000]
print(to_sum)
print(sum(to_sum))







