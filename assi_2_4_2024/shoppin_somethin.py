# Storing items in a dictionary
d = {'apple': 100, 'orange': 120, 'potato': 150, 'onion': 200}

# Taking user input for budget
b = int(input('Enter your budget: '))
print("Available items and their prices:")
print(d)

# Taking user input for the item name and quantity
o = input("Enter the item name you want to buy: ")
q = int(input("Enter the quantity you want to buy: "))

# Calculating the total cost for the selected item and quantity
def total(item, quantity, prices):
    return prices.get(item, 0) * quantity

t = total(o, q, d)

# Checking if the total cost is within budget
def check_budget(total_cost, budget):
    if total_cost <= budget:
        return "Within budget"
    else:
        return "Out of budget"

r = check_budget(t, b)

# Printing the results
print(f"Total cost for {q} {o}(s) is {t}")
print(f"Budget status: {r}")
