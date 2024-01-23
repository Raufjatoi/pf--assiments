def crops (s,t,r,sl):
    if s == "summer" and t > 30 and r > 400 :
        return "Rice"
    elif s == "summer" and t > 35 and sl == "sandy":
        return "cotton"
    elif s == "summer" or "winter" and t >=25 and t <=30:
        return "bajra"
s = input("Enter season : ").lower()
t = int(input("Enter your temp : "))
r = int(input("Enter rainfall : "))
sl = input("enter soil : ")
print(crops(s,t,r,sl))
