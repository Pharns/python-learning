# --- Welcome ---#
print("Welcome to the tip calculator!")

# --- Inputs ---#
total_bill = float(input("What was the total bill? "))
tip_percentage = float(input("How much tip would you like to give? 10, 12,or15? "))
number_people = float(input("How many people to split the bill? "))

# --- Calculation ---#
amount_due = round(
    (total_bill + (total_bill * (tip_percentage / 100))) / number_people, 2
)

# --- Output ---#
print(f"Each person should pay: ${amount_due:.2f}")
