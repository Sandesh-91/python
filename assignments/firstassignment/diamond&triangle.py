no=int(input("Enter no of rows"))
sum=""
for x in range(1,no+1):
    sum+=" " * (no-x) + "*" * (2*x-1)+ "\n"
for y in range(no-1,0,-1):
    sum+=" " * (no-y) + "*" * (2*y-1) + "\n"
print("Diamond \n")
print(sum)

hold=""
for x in range(1,no+1):
    hold+=" " * (no-x) + "*" * (2*x-1)+ "\n"
print("Triangle \n")
print(hold)
#diamond and triangle