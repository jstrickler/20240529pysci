my_list = list()  # empty list
my_other_list = []  # empty list

cities = ['Portland', 'Pittsburg', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)   # add elements one at a time
print(f"cities: {cities}\n")

#  LIST.append(obj)   LIST.insert(pos, object)   LIST.extend(iterable)

del cities[3]    # del is not a function -- don't use ()
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

cities = ['Boston', 'Portland', 'Pittsburg', 'Miami', 'Buffalo', 'Montgomery', 'Detroit', 'Des Moines']

print(f"{cities[2] = }")
print(f"{cities[0] = }")
print(f"{cities[7] = }")
print(f"{len(cities) = }")
print(f"{cities[-1] = }")  # cities[len(cities) - 1]
print(f"{cities[-2] = }")
# print(f"{cities[22] = }")

name = "Frank"
print(f"{name[0] = }")
print(f"{name[-1] = }")
print(f"{name[2] = }")

print(f"{cities = }")

# slice
#  LIST[start-at:stop-before:count-by]
print(f"{cities[0:4] = }")  # 0 through 3
print(f"{cities[4:7] = }")  # 4 through 6
print(f"{cities[:4] = }")  # first 4
print(f"{cities[5:] = }")  # 5 through end
print(f"{cities[-3:] = }")  # last 3

state = "North Carolina"
print(f"{state[6:11] = }")
print(f"{state[:3] = }")

# for VAR in ITERABLE:
#     ...

for city in cities:
    if city.startswith('B'):
        print(city)
    elif city.startswith('P'):
        print(city.upper())


