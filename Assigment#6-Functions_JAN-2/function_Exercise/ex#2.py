#Write a program for a temperature converter. Prompt the user to enter a temperature in Celsius.
#If the temperature is below freezing (0°C or lower), print a message recommending to wear warm clothes. If it's above 30°C, suggest staying hydrated.
while True:
 f = int(input("enter temp in c : "))
 if f < 1:
    print("weaar warm cloths ")
 elif f > 30:
    print("Stay hydrated ")
 else:
    print("temp is moderate ")