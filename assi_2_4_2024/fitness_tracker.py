s = int(input('Enter today\'s steps: '))
# Supposing the week's total steps should be 
w = s * 7
# Imagining 10 steps cost 2 cal 
c = s / 5 
# Imagine 10 steps = 1m 
d = s / 10
# Monthly distance covered be like then 
dc = d * 30  # It can be 31 too

def fitness_tracker(w, dc):
    def avg_steps(w):
        return w / 7

    avg_steps_week = avg_steps(w)

    def avg_dis(dc):
        return dc / 30

    avg_distance_is = avg_dis(dc)

    return avg_steps_week, avg_distance_is

avg_steps_week, avg_distance_is = fitness_tracker(w, dc)
print(f"You covered a total distance of {d:.0f} meters.")
print(f"You burned {c:.0f} calories.")
print(f"Average steps per week should be {avg_steps_week:.0f}.")
print(f"Avg distance covered by you in a month is {avg_distance_is:.0f}.")
