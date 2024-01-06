#Build a function that estimates the travel cost for a chosen destination, considering transportation, accommodation, and activities.
#Include options for different travel styles (budget, luxury) and durations.

trans = input("enter ur transportation vehicle /bus/train/car/etc :: ").lower()
des = input("enter ur destination /karachi/lahore/nawabshah :: ").lower()
status = input("enter ur traveling status /budget/luxary :: ").lower()

price = 0
def transportation():
    global trans
    global price
    if trans == "bus":
        price = 500
    elif trans == "train":
        price = 1000
    elif trans == "car":
        price = 1200
    else:
        price = 600
    return price

    
price1 = 0
distance = ()
def destination():
    global des 
    global price1
    global distance 
    if des == "karachi":
        price1 = 200
        distance = "1000 kms"
    elif des == "lahore":
        price1 = 400
        distance = "5000 kms"
    elif des == "nawabshah":
        distance = "500"
        price1 = 100
    return price1,distance

price3 = 0
def trans_status():
    global status 
    global price3
    if status == "budget":
        price3 = price + price1 + 500
    elif status == "luxary":
        price3 = price + price1 + 1000
    else:
        price3 = price + price1 + 100

transportation()
destination()
trans_status()

print(f"your travel vehicle price is {price}")
print(f"ur destination distance is {distance}")
print(f"ur destination fee is {price1}")
print(f"ur travelling status is {status}")
print(f"ur total price is {price3}")