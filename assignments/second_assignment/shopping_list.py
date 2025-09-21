shoppingList={}
def addItem():
    name=input("Name of product ")
    price=float(input("Enter price of product "))
    quantity=str(input("Enter quantity of product "))
    shoppingList[name]={"Name":name, "price":price,"quantity":quantity}
def viewItem():
    if not shoppingList:
        print("Shopping List is empty ")
        print("\n Items in your List are: ")
    for name,details in shoppingList.items():
        print(f"Name: {name} , Price: Rs.{details["price"]}, Quantity: {details["quantity"]}")
def removeItem():
    name=input("Enter the name of item that you want to remove: ")
    if name in shoppingList:
        del shoppingList[name]
        print(f"{name} removed successfully ")
    else:
        print(f"{name} doesnot exist ")
        

while True:
    print("1: Add item \n2: View item \n3: Remove item \n4: Exit ")
    ch=int(input("Enter your choice: "))
    match ch:
        case 1:
            addItem()
        case 2:
            viewItem()
        case 3:
            removeItem()
        case 4:
            print("Exiting ")
            break
        case _:
            print("Invalid input ")
