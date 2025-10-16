### Lists
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

### Welcome ###
# print("\nWelcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like\n"))

import random

password = []
num = random.randint(0, 24)
### Letters ###
for letter in range(nr_letters):
    num = random.randint(0, 24)
    password.append(letters[num])

### Symbols ###
for symbol in range(nr_symbols):
    num = random.randint(0, 8)
    password.append(symbols[num])

### Numbers ###
for number in range(nr_numbers):
    num = random.randint(0, 8)
    password.append(numbers[num])

random.shuffle(password)
final_password = "".join(password)
print(f"Your password is {final_password}")

# ## 2nd way
# password = ""

# for char in rage (1,nr_letters +1):
#     password += rand.choice(letters)
