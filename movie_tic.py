"""
day = input("Enter a day: ").lower()
age = int(input("Enter your age: "))
#### MOd
fam = input("are ya with fam ::( y/n )").lower()
ticket = 0
ticket1 = 0
family_discount = 0

def calculate_ticket_price():
    global ticket
    if day == "monday":
        ticket = 1000
    elif day == "tuesday":
        ticket = 900
    elif day == "wednesday":
        ticket = 800
    elif day == "thursday":
        ticket = 700
    elif day == "friday":
        ticket = 600
    elif day == "saturday":
        ticket = 500
    elif day == "sunday":
        ticket = 1200
    else:
        print("Invalid day")
        return calculate_ticket_price()

def calculate_discount():
    global ticket1
    if age < 18:
        ticket1 = ticket - 50
    elif 18 <= age < 25:
        ticket1 = ticket - 30
    else:
        ticket1 = ticket - 100

#### MODIFICATION FOR DEALS OR FAMILY DISCOUNT

def fam():
    global family_discount
    if fam in ["ye","yesh","yep","y"]:
        family_discount = ticket1 - 40
    elif fam in ["no","nope","nah","noo","n"]:
        family_discount = "No discount "
    else:
        family_discount = "no Answer"
    return fam
        

calculate_ticket_price()
calculate_discount()

print(f"Your ticket price is {ticket}")
print(f"After discount, it is {ticket1:.2f}")
print(f"family discount is {family_discount}")

"""

#### CHATGPT 

day = input("Enter a day: ").lower()
age = int(input("Enter your age: "))
fam_input = input("Are you with family? (y/n): ").lower()
ticket = 0
ticket_after_discount = 0
family_discount = 0

def calculate_ticket_price():
    global ticket
    if day == "monday":
        ticket = 1000
    elif day == "tuesday":
        ticket = 900
    elif day == "wednesday":
        ticket = 800
    elif day == "thursday":
        ticket = 700
    elif day == "friday":
        ticket = 600
    elif day == "saturday":
        ticket = 500
    elif day == "sunday":
        ticket = 1200
    else:
        print("Invalid day")
        return calculate_ticket_price()

def calculate_discount():
    global ticket_after_discount
    if age < 18:
        ticket_after_discount = ticket - 50
    elif 18 <= age < 25:
        ticket_after_discount = ticket - 30
    else:
        ticket_after_discount = ticket - 100

def apply_family_discount():
    global family_discount
    if fam_input in ["ye", "yesh", "yep", "y","yes"]:
        family_discount = ticket_after_discount - 40
    elif fam_input in ["no", "nope", "nah", "noo", "n"]:
        family_discount = "No discount"
    else:
        family_discount = "No answer"

calculate_ticket_price()
calculate_discount()
apply_family_discount()

print(f"Your ticket price is {ticket}")
print(f"After discount, it is {ticket_after_discount:.2f}")
print(f" Family discount is 40 rs ")
print(f" After fam discpunt is {family_discount}")
