#Question 5: Online Shopping Cart
#Develop a Python program for an Online Shopping Cart. Create a function checkout(cart_total) that 
#takes the total cost of items in the cart and applies a discount based on the user's membership level. 
#Regular members get a 5% discount, premium members get a 10% discount, and VIP members get a 
#15% discount


total_cost = int(input("Enter total cost: "))
um = input("Enter your membership level (regular/premium/vip): ").lower().strip()
fiv = total_cost * 0.05
ten = total_cost * 0.10
fifty = total_cost * 0.15

def checkout(cart_total):
    if "regular" in um:
        print(f"Your total is {total_cost} after 5% discount it is {total_cost - fiv:.1f}")
    elif "premium" in um:
        print(f"Your total is {total_cost} after 10% discount it is {total_cost - ten:.1f}") 
    elif "vip" in um:
        print(f"Your total is {total_cost} after 15% discount it is {total_cost - fifty:.1f}")
    else:
        print("Invalid input")

checkout(total_cost)



