#Question 1: Crop Monitoring System
#Imagine you are developing a Crop Monitoring System for farmers. Write a Python function 
#monitor_crop(temperature, humidity, rainfall) that takes environmental conditions as input and returns 
#"Watering needed" if the humidity is low and rainfall is below average, and "Optimal conditions" 
#otherwise.
t = float(input("Enter temperature: "))
h = input("Enter humidity (low/high): ").lower()
r = input("Enter rainfall (high/low(below avg)): ").lower()

def monitor_crop(temperature, humidity, rainfall):
    if humidity == "low" and rainfall == "low":
        print("Watering needed")
    else:
        print("Optimal conditions")

monitor_crop(t, h, r)
