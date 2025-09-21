#in python file handling has 

"""this many modes:
read-r
write-w
append-a
create new file and return error if already exists-x


In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


the advantage of using with is that it removes the overhead of closing the files manually
"""


#creatin a  new file 

# f=open("First.txt","x")

#opening file 
with open("First.txt","w") as f:

#writing to the file 
    f.write("hello this is my first file in python")

#closing the file is important when not using with
# f.close()

#now reading from the file 

with open("First.txt") as f:
    value=0
    #reading 
    fetch=f.read()
    #count the number of words
    word=input("enter the word to count frequency: ")
    count=fetch.split()
    for x in count:
        if x==word:
            value+=1
    print(f"The frequency of {word} in FILE is {value}")
    length=len(count)
    print(f"Total words in file are {length}")
    print(fetch)

