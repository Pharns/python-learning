## Input
word = input("Enter a word: ").lower()

## Reverse the word
reverse_word = word[::-1]
print(reverse_word)

## Ouput
if word == reverse_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
