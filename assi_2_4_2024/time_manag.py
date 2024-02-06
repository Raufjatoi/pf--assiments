a = {}

for i in range(3):
    activity = input('Enter activity: ')

    while True:
        try:
            time_spent = float(input('Enter time spent on it (in hours): '))
            break
        except ValueError:
            print('Invalid input. Please enter a numerical value for time.')

    a[activity] = time_spent

print("Activities and time spent:")
print(a)
total_time = sum(a.values())
print(f"Total time spent: {total_time} hours")
max_time_activity = max(a, key=a.get)
min_time_activity = min(a, key=a.get)
print(f"Area for improvement: {min_time_activity} (min time spent)")
print(f"Strong area: {max_time_activity} (max time spent)")
