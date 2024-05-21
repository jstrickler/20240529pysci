import sys   # Import the sys module 

print(sys.argv) # Print all parameters, including script itself

print(sys.argv[0])  # script name

name = sys.argv[1]  # Get the first actual parameter
print("name is", name)
