counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for line in breakfast_in:
        # print(counts)
        # print('-' * 60)
        food = line.rstrip()
        if food in counts:   # is food a key in the dict?
            counts[food] = counts[food] + 1
        else:
            counts[food] = 1
    
print('=' * 60)

for food, count in counts.items():
    print(food, count)
