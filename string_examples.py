person = "Taylor Swift"

print(type(person))
print(len(person))

x = person.upper()
print(x)
print(person.upper())
print(person.count('t'))
print(person.count('T'))
print(person.lower().count('t'))   # method chaining 

print("abc".upper())

names = person.split()
print(names)

print(person.startswith('Tay'))
print(person.startswith('Bob'))

print(person.removesuffix(' Swift'))

lyric = "     All my exes live in Texas     "
print('|' + lyric + '|')
print('|' + lyric.lstrip() + '|')
print('|' + lyric.rstrip() + '|')
print('|' + lyric.strip() + '|')
print()

amount = "        $234.88"
a2 = amount.lstrip('$ ')
print(amount, a2)


print(person.find('Taylor'))
print(person.find('Swift'))
print(person.find('Tom'))

print("Taylor" in person)
print("Tom" in person)

print(person.replace('Taylor', 'Tom'))
p2 = person.replace('Taylor', 'Tom')
print(p2, person)
