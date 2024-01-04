def calculate_total_bill(ordered_items, quantities, prices, discount_percentage=0, tax_percentage=0, split_bill=False, num_friends=1):
    # Assume prices is a dictionary mapping each item to its price
    # Example: prices = {'item1': 10, 'item2': 20, 'item3': 15}

    # Ensure quantities is a list
    if isinstance(quantities, int):
        quantities = [quantities] * len(ordered_items)

    # Calculate total cost before discounts and taxes
    total_cost = sum(quantities[i] * prices[item] for i, item in enumerate(ordered_items))

    # Apply discount
    if discount_percentage > 0:
        discount_amount = (discount_percentage / 100) * total_cost
        total_cost -= discount_amount

    # Apply tax
    if tax_percentage > 0:
        tax_amount = (tax_percentage / 100) * total_cost
        total_cost += tax_amount

    # Split the bill among friends
    if split_bill and num_friends > 1:
        total_cost /= num_friends

    return total_cost

# Example usage:
ordered_items = ['item1', 'item2', 'item3']
quantities = [2, 1, 3]  # Assuming the quantities are in the same order as the items
prices = {'item1': 10, 'item2': 20, 'item3': 15}
discount_percentage = 10
tax_percentage = 5
split_bill = True
num_friends = 3

total_bill = calculate_total_bill(ordered_items, quantities, prices, discount_percentage, tax_percentage, split_bill, num_friends)
print(f'Total Bill Amount: ${total_bill:.2f}')
