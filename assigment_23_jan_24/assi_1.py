def recommend (temp,rain):
    if temp > 25 and rain > 50:
        print("Dont give water ")
    elif temp > 25 and rain < 50:
        print('give water to crops ')
    elif temp < 25:
        print("Temperature is moderate , dont give water to crops ")
    else:
        print("invalid input")
while True:
 temp = int(input("Enter temp today : "))
 rain = int(input("Enter rain today : "))
 recommendation = recommend(temp,rain)
 res = input("Do you want to continue : ").lower()

 if res != "yes" or "y":
     break
