count=0
for x in range(1000,3000):
    if x % 7 == 0 and x % 5 !=0:
        print(f"{x}")
        count+=1
print(count)   