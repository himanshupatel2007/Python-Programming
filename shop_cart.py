items = ["Apple", "Banana", "Orange"]
print("List :")
for i in items :
    print(f"{i}")
fruit = input("Enter the Fruit : ")
quantity = int(input("Enter the Quantity : "))
if fruit == "Apple" or fruit == "apple" : print(f"Total : {quantity * 10}")    
elif fruit == "Banana" or fruit == "banana" : print(f"Total : {quantity * 5}")    
elif fruit == "Orange" or fruit == "orange" : print(f"Total : {quantity * 8}")    
else : print("Item does not exist in the List!")
