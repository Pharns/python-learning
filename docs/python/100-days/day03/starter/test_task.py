# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.00")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.00")
#     elif 45 >= age <=55:
#         print("Have a free rid on us")
#     else:
#         bill = 12
#         print("Adult tickets are $12.00")
#     wants_photo = input("Do you want a phot? Type y for Yes or n for No")
#     if wants_photo == "y":
#         bill += 3
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry you can't ride the rollercoaster")


# input = int(input("Enter a number "))
# number = input % 2
# if number == 0:
#    print("Your number is even!")
# else:
#    print("Your number is odd!")


print("Welcome to Pythong Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2
elif size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3
elif size == "l":
    bill = 25
    if pepperoni == "y":
        bill += 3
if extra_cheese == "y":
    bill += 1
else:
    print("Invalid size selected")

print(f"Your final bill is ${bill}")
