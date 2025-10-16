##  Inputs
first = int(input("Enter 1st number: \n"))
second = int(input("Enter 2nd number: \n"))
third = int(input("Enter 3rd number: \n"))
fourth = int(input("Enter 4th number: \n"))
fifth = int(input("Enter 5th number: \n"))

## Input list
inputs = [first, second, third, fourth, fifth]

## Calculations & Conversions
float_sum_value = float(sum(inputs))
integer_sum_value = int(sum(inputs))
string_sum_value = str(first) + str(second) + str(third) + str(fourth) + str(fifth)

## Output
print(f"Integer: {integer_sum_value}")
print(f"Float: {float_sum_value:.1f}")
print(f"String: {string_sum_value}")
