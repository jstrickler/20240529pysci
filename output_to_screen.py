person = "Taylor Swift"
city = "Los Angeles"
amount = 37.43893930394

print(person)
print(person, city, amount)
print(person, city, amount, sep=",")
print(person, city, amount, sep=", ")
print(person, city, amount, sep="--")
print(person, city, amount, sep="")
print()
print(person, end=" ")
print(amount)
#  str(person) + sep + str(city) + sep + str(amount) + end

fs = f"{city}: {person}"
print(fs)

print(f"{person} lives in {city}")
print(f"2 + 2 is {2 + 2}")

print(f"amount is {amount}")
print(f"amount is {amount:.2f}")
count = 73
print(f"Count is {count:4d}")
print(f"Count is {count:04d}")


