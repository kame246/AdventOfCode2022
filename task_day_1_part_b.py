with open('input_1a_temp.txt') as f:
    elfs_calories = f.read().split('\n\n')

results = []
for calories in elfs_calories:
    results.append(sum([int(c) for c in calories.split('\n')]))

print('Answer:', sum(sorted(results, reverse=True)[:3]))




