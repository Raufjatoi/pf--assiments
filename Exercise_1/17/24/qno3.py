#Question 3: Ride-Sharing Fare Calculator
#You are working on a Ride-Sharing Fare Calculator. Develop a Python function calculate_fare(distance, 
#time_of_day) that takes the distance of the ride and the time of day as input and returns the fare. Apply 
#a 20% surcharge during peak hours (8 am - 10 am and 5 pm - 7 pm) and a 10% discount for late-night 
#rides (10 pm - 5 am).
def calculate_fare(distance, time_of_day):
    base_fare_per_unit = 1.5  # Adjust this value based on your pricing model
    peak_hour_surcharge = 0.2
    late_night_discount = 0.1

    # Convert distance to numeric value
    try:
        distance = float(distance)
    except ValueError:
        print("Invalid distance input. Please enter a numeric value.")
        return

    # Check if the time of day is during peak hours
    is_peak_hour = (time_of_day >= 8 and time_of_day <= 10) or (time_of_day >= 17 and time_of_day <= 19)

    # Check if the time of day is during late night
    is_late_night = time_of_day >= 22 or time_of_day < 5

    # Apply surcharge or discount accordingly
    if is_peak_hour:
        fare = base_fare_per_unit * distance * (1 + peak_hour_surcharge)
    elif is_late_night:
        fare = base_fare_per_unit * distance * (1 - late_night_discount)
    else:
        fare = base_fare_per_unit * distance

    return fare

# Example usage:
distance_input = input("Enter your distance (kms/miles): ")
time_input = int(input("Enter the time of day (24-hour format): "))

fare = calculate_fare(distance_input, time_input)

if fare is not None:
    print("Your fare is:", fare)

