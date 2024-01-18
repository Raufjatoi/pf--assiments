#Question 4: Health Tracker App
#Create a function check_activity_goal(steps_taken, goal) for a Health Tracker App. If the user has 
#achieved their daily step goal (given as input), return "Goal achieved," otherwise, provide a message 
#indicating how many more steps are needed to reach the goal.
goal = int(input("Enter your goal : "))
steps_taken = int(input("Enter how many steps ya taken : "))

def check_activity_goal(steps_taken,goal):
    if steps_taken >= goal:
        print("Goal acheached")
    elif steps_taken < goal:
        print(f"{goal-steps_taken} steps needed to complete the Goal")
    else:
        print("invalid input")

check_activity_goal(steps_taken,goal)