## Write a program that asks for two numbers and prints
## their sum, difference, product, and quotient (formatted cleanly).

number1 = int(input("Pick your first number: "))
number2 = int(input("Pick your second number: "))

# calculating the sum
total_sum = sum([number1, number2])
print(f"Your total sum is {total_sum}")

# calculating the difference
total_difference = number1 - number2
print(f"The difference is {total_difference}")

# calculating the product
total_product = number1 * number2
print(f"The product is {total_product}")

# calculating the quotient
total_quotient = number1 / number2
print(f"The quotient is {total_quotient:.2f}")
