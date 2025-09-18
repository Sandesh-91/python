var = 0
n = int(input("Enter a number: "))
if n == 1 or n == 0:
    print(f"{n} is neither prime nor composite: ")
else:
    for x in range(2, n // 2 +1):
        if n % x == 0:
            var = 1
            break
    if var:
        print(f"{n} is composite: ")
    else:
        print(f"{n} is  prime: ")