#Develop a program for an online shopping cart. Prompt the user to enter the quantity and price of three items.
#Calculate and print the total cost. Apply a 5% discount if the total cost is between $100 and $200, and a 10% discount if it's above $200.
x = 0
for i in range (3):
    q = int(input("how much quantity u buy :"))
    p = int(input("what is price of quantity:"))
    x = x + p * q 
print(f"Total cost is {x}" )
if  x > 100 and x < 200 :
    print("5% Discount applied")
    print(f"after discount is {x*0.5}")
elif x > 200:
    print("10% Discount applied")
    print(f"aftee discount is {x*0.10}")
else:
    print("no discount")
    print(f"total price is {x}")



