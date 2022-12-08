with open('input_7a_real.txt') as f:
    lines = f.readlines()

from pathlib import Path
pwd = Path('/')
disk = {}
num_line = 0
total_size = 70000000
while num_line < len(lines):
    line = lines[num_line]
    if line.startswith('$'):
        line = line.rstrip()
        command, *params = line[2:].split(' ')
        if command == 'cd':
            if params[0] == '..':
                pwd = pwd.parent
            elif params[0].startswith('/'):
                pwd = Path(params[0])
            else:
                pwd = pwd / params[0]
        elif command == 'ls':
            while num_line < len(lines)-1 and not lines[num_line + 1].startswith('$'):
                num_line += 1
                line = lines[num_line].rstrip()
                a, b = line.split(' ')
                if a == 'dir':
                    dir_path = pwd / b
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
        num_line += 1

def calc_size(path):
    s = 0
    for f in disk[path]:
        s += f if isinstance(f, int) else calc_size(f)
    return s

for path in disk:
    disk[path] = calc_size(path)

candidates = sorted([x for x in disk.values()])
free_space = total_size - candidates[-1]
for c in candidates:
    if free_space + c >= 30000000:
        print(c)
        break








