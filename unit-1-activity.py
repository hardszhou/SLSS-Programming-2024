# Unit 1 Activity
# Author: Hardy
# 4 March 2024

def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi

def bmi_result(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Regular weight"
    else: "Overweight"

def main():
    print()
    print("Welcome to the BMI Calculator!\n")
    print("This calculates your body mass index from your weight and height.\n")
    weight = float(input("Enter your weight in kilograms: \n"))
    print()
    height = float(input("Enter your weight in meters: \n"))

    print()
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi}\n")

    bmi_category = bmi_result(bmi)
    print(f"You are: {bmi_category}\n")

main()