#Question 6: Weather App
#Imagine building a Weather App. Write a function weather_advice(temperature, precipitation) that 
#provides advice based on the current weather conditions. If it's hot and sunny, suggest wearing 
#sunscreen; if it's raining, recommend carrying an umbrella; and if it's cold, suggest dressing warmly.

tem = int(input("Enter temperature: "))
p = input("How's the weather there (raining/sunny): ").lower()

def weather_advice(temperature, precipitation):
    if temperature <= 30:
        print("Wear some warm clothes.")
    elif 31 <= temperature <= 40:
        if precipitation == "rainy":
            print("Use an umbrella.")
        elif precipitation == "sunny":
            print("Wear sunscreen and stay hydrated.")
        else:
            print("Invalid input for precipitation.")
    elif temperature > 40:
        print("It's very hot! Wear sunscreen and stay hydrated.")
    else:
        print("Invalid input for temperature.")

weather_advice(tem, p)


