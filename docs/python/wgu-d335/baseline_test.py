with open("words.txt", "r") as file:
    words = file.read().splitlines()
print(words)

sentence = " ".join(words)

print(sentence)
