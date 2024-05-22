COLOR = "blue"  # global variable

def spam():
    COLOR = "green"
    animal = "honey badger"   # local variable
    print(f"{COLOR = }")
    
spam()

print(f"{COLOR = }")
