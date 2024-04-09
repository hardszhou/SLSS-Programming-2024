# Mid Term Activity
# Author: Hardy
# 9 April 2024

def calculate_calories_burned(activity, duration_in_minutes, weight):
    if activity.lower() == "running":
        calories_per_minute = 7.5
    elif activity.lower() == "cycling":
        calories_per_minute = 5.0
    else:
        calories_per_minute = 4.0
    total_calories_burned = calories_per_minute * duration_in_minutes * (weight / 70)
    return total_calories_burned

activity = input("Enter the activity (e.g., running, cycling): ")
duration = int(input("Enter the duration of the workout in minutes: "))
weight = float(input("Enter your weight in kilograms: "))

calories_burned = calculate_calories_burned(activity, duration, weight)
print("You burned approximately", calories_burned, "calories during your workout.")

for i in range(3):
    print("Keep up the good work!")