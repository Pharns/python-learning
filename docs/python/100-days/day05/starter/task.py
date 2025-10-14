# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# print(fruits)

# student_scores = [
#     150,
#     142,
#     185,
#     120,
#     171,
#     184,
#     149,
#     24,
#     59,
#     68,
#     199,
#     78,
#     65,
#     89,
#     86,
#     55,
#     91,
#     64,
#     89,
# ]
# # print(max(student_scores))
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)


# RANGE FUNGTION
# for number in range(a,b):
# print

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# fizzbuzz = 0
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
