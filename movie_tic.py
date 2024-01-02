day = input("Enter a day: ").lower()
age = int(input("Enter your age: "))
ticket = 0
ticket1 = 0

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
        ticket1 = ticket / 20
    elif 18 <= age < 25:
        ticket1 = ticket / 15
    else:
        ticket1 = ticket / 25

calculate_ticket_price()
calculate_discount()

print(f"Your ticket price is {ticket}")
print(f"After discount, it is {ticket1:.1f}")

