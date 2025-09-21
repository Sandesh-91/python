def fibonacci(n):
    if n==0:
        return n
    if n<=2:
        return n-1
    else :
        return  fibonacci(n-1)+fibonacci(n-2)
no=int(input("Enter how many Fibonacci numbers do you want: "))
for i in range(0, no):
    print(fibonacci(i))