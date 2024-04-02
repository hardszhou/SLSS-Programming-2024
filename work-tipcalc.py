# Tip Calc
# Author: Hardy
# 28 February 2024

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    # Note: This is one way to round a number to two decimal places
    print(f"Leave ${round(tip, 2)}")


def dollars_to_float(d):
    # Converts string dollars to a decimal float
    #    Returns the result
    dollars = float(d)
    return dollars


def percent_to_float(p):
    # Converts percent to a decimal float
    #    Returns the result
    percent = float(p)/100
    return percent

main()