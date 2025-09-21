with open("Frequency.txt","w") as f:
    f.write("Hello! My name is Sandesh Aryal Hello! Sandesh")
with open("Frequency.txt") as f:
    fetch=f.read()
    count=fetch.split()
    total=len(count)
    for x in range(total):
        value=0
        for y in range(total):
            if count[x]==count[y]:
                value+=1
        if count[x] not in count[:x]:
            print(f"The word {count[x]} is repeated {value} times")