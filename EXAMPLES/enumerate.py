
colors = "red blue green yellow brown black".split()

months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

enum_colors = enumerate(colors)
print(f"{enum_colors = }")

for i, color in enum_colors:  # enumerate() returns iterable of (index, value) tuples
    print(i, color)

print()

for num, month in enumerate(months, 1):  # Second parameter to enumerate is added to index
    print(f"{num} {month}")
print('-' * 60)

rev_colors = reversed(colors)
print(f"{rev_colors = }")
for color in rev_colors:
    print(color, end=', ')
print('\n')

capitals = 'Raleigh', 'Richmond', 'Annapolis'
states = 'NC', 'VA', 'MD'

info = zip(capitals, states)
print(f"{info = }")
print(list(info))

info = zip(capitals, states)
for capital, state in info:
    print(capital, state)






