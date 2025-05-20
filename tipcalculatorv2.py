import math

#tip calculator
try:
    cost = float(input("What was the total bill?: $"))
    tipx = (input("What percentage tip would you like to give?: "))
    tipf = float(tipx) / 100
    tip = cost * tipf

    print(f"The tip is: ${tip:.2f}")
except ValueError:
    print("Please enter a valid number.")



