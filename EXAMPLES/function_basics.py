def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, Python world"  # Function returns value

get_hello()

h = get_hello()  # Store return value in h
print(h)
print(get_hello())  # print value returned by get_hello()

# type hints/hinting

#       parameter
def sqrt(polar_bear):  # Function takes exactly one argument
    return polar_bear ** .5

#       argument
m = sqrt(1234)  # Call function with one argument
n = sqrt(2)
wombat = 27
print(f"{wombat = }")

#           argument 
print(f"{sqrt(wombat) = }")
v = 98
result = sqrt(v)


print(f"m is {m:.3f} n is {n:.3f}")

def whoosh(a, b, c):
    print(f"{a = }")
    print(f"{b = }")
    print(f"{c = }\n")

whoosh(5, 10, 15)

def blutz(a, *b):
    print(f"{a = }")
    print(f"{b = }\n")

blutz(5, 10, 15, 20)
blutz(5)

def get_number_of_lines(file_path):
    with open(file_path) as file_in:
        count = 0
        for line in file_in:
            count += 1
    return count

line_count = get_number_of_lines('../DATA/parrot.txt')
print(f"{line_count = }")

file_name = '../DATA/words.txt'
print(f"{get_number_of_lines(file_name) = }")











