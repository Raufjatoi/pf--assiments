# Recipe Calculator
servings = int(input("Enter the number of servings: "))

rice_per_serving = 100
chicken_per_serving = 50  

total_rice = rice_per_serving * servings
total_chicken = chicken_per_serving * servings

print(f"For {servings} servings, you'll need:")
print(f"{total_rice} grams of rice")
print(f"{total_chicken} grams of chicken")
