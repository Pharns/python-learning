# list of mixed data elements
data_mixture = [
    "Python is fun",
    2024,
    5.67,
    ["apple", "banana", "coconut"],
    None,
    {"name": "John", "age": 25},
]

# input for index
print("Enter index:")
index = int(input())

element = data_mixture[index]
data_type = type(element).__name__

if isinstance(element, (list, str, dict)):
    message = "This element is iterable."
elif isinstance(element, (int, float)):
    message = "This element is numeric."
else:
    message = "This is a different data type."

print(f"Element: {element}, Type: {data_type}, Message: {message}")
