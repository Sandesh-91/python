def addContact():
    with open("contacts.txt","a") as f:
        name=input("Enter name: ").capitalize()
        while True:
            number=(input("Enter number: "))
            if number.isdigit() and len(number)==10:
                break
            else:
                print("Invalid input ")
        f.write(f"Name: {name} , Number: {(number)}\n")
        print("\nContact added ")
def viewContact():
    with open("contacts.txt") as f:
        print(f.read())
def removeContact():
    name_to_remove=input("Enter the name that you want to remove from contacts: ").capitalize()

    with open("contacts.txt") as f:
        line=f.readlines()
    with open("contacts.txt","w") as f:
        for x in line:
            if name_to_remove in x:
                continue
            f.write(x)
while True:
    print("\n1: Add contact \n2: View contact \n3: Remove contact \n4: Exit ")
    ch=int(input("\nEnter your choice: "))
    match ch:
        case 1:
            addContact()
        case 2:
            viewContact()
        case 3:
            removeContact()
        case 4:
            print("Exiting ")
            break
        case _:
            print("Invalid input ")


