count = 0
ranges = []
with open('input_4a_real.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        elf1, elf2 = line.split(',')
        a, b = elf1.split('-')
        a = int(a)
        b = int(b)
        c, d = elf2.split('-')
        c = int(c)
        d = int(d)
        r1 = set(range(a, b + 1))
        r2 = set(range(c, d + 1))
        if len(r1.intersection(r2)) > 0:
            count += 1


print(f'{count=}')