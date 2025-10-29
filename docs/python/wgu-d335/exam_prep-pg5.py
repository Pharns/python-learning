# Write a Python program that:
# Asks the user for a short sentence.
# Saves that sentence into a file called message.txt.
# Reads the sentence back from the file.
# Prints the exact contents that were read.

# Ask user for input
sentence = input("Enter a short sentence: ")

# Save input to file
with open("message.txt", "w") as file:
    file.write(sentence)

# Read content
with open("message.txt", "r") as file:
    content = file.read()

print(f"Your file says: {content}")
