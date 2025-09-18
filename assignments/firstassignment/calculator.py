a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Enter choice: ")
print("1 for Addition: ")
print("2 for Subtraction: ")
print("3 for Multiplication: ")
print("4 for Division: ")
choice=int(input("Enter choice: \n"))
match choice:
    case 1:
        print(f"{a} + {b} = {a+b}\n")
    case 2:
        print(f"{a} - {b} = {a-b}\n")
    case 3:
        print(f"{a} * {b} = {a*b}\n")
    case 4:
        print(f"{a} / {b} = {a//b}\n")
    case _:
        print("Invalid input ")


