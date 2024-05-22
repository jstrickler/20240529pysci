
def spam(greeting, whom='world'):  # 'world' is default value for positional parameter whom
    print(f"{greeting}, {whom}")

spam("Hello", "Mom")  # parameter supplied; default not used
spam("Hello")  # parameter not supplied; default is used
print()

