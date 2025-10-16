##  Predefined List
predef_list = [4, -27, 15, 33, -10]


## Defined Function
def is_in_list(value):
    return value in predef_list


# Input
value = int(input())

# Function Call
Boolean_value = is_in_list(value)

# Ouput
print(f"Is the input present in the list? {Boolean_value}")


# number = int(input("Is this number in the list?"))
