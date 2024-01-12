#Build a program for a small business inventory. Allow the user to add items (name, quantity, and price) to a list of dictionaries.
# Print the inventory and calculate the total value.
"""
dict1 = {}
l1 = []
l2 = []
l3 = []
for i in range (3):
    name = input("Enter a name : ")
    quantity = int(input("Enter quantity : "))
    price = float(input("Enter price : "))
    l1.append(name)
    l2.append(quantity)
    l3.append(price)
print(l1)
print(l2)
print(l3)
dict1.append(l1,l2,l3)
print(dict1)

"""

inventory = []

for i in range(3):
    name = input("Enter a name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    item = {
        'name': name,
        'quantity': quantity,
        'price': price
    }

    inventory.append(item)

# Print the inventory
print("Inventory:")
for item in inventory:
    print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")

# Calculate the total value
total_value = sum(item['quantity'] * item['price'] for item in inventory)
print(f"Total Value of Inventory: ${total_value}")
