# --- Welcome ---#
print("Welcome to the tip calculator!")

# --- Inputs ---#
<<<<<<< HEAD
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_people = int(input("How many people to split the bill? "))
=======
total_bill = float(input("What was the total bill? "))
tip_percentage = float(input("How much tip would you like to give? 10, 12,or15? "))
number_people = float(input("How many people to split the bill?"))
>>>>>>> 6a9e233c650b5ea91f33bcdf4d87bbcdf4ea45ad

# --- Calculation ---#
amount_due = round(
    (total_bill + (total_bill * (tip_percentage / 100))) / number_people, 2
)

# --- Output ---#
<<<<<<< HEAD
print(f"Each person should pay: ${amount_due:.2f}")
=======
print(f"Each person should pay: {amount_due}")
>>>>>>> 6a9e233c650b5ea91f33bcdf4d87bbcdf4ea45ad
