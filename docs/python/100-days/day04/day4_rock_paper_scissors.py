rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

### Players Input ###
print("Welcome to Rock, Paper, Scissors!")
choice1 = int(
    input(
        "What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"
    )
)
if choice1 == 0:
    print(rock)
    print("You chose rock")
elif choice1 == 1:
    print(paper)
    print("You chose paper")
elif choice1 == 2:
    print(scissors)
    print("You chose scissors")
else:
    print("Not a valid input!")
    exit()

### Computer Choice ###
import random

game_list = [rock, paper, scissors]
computers_choice = random.randint(0, 2)
print(game_list[computers_choice])
names = ["rock", "paper", "scissors"]
# print(f"\n The computer chose {names[computers_choice]}")
print(f"The computer chose {names[computers_choice]}\n")

### Winner Logic ###
if choice1 == computers_choice:
    print("It's a tie.\n")
elif (
    (choice1 == 0 and computers_choice == 2)
    or (choice1 == 1 and computers_choice == 0)
    or (choice1 == 2 and computers_choice == 1)
):
    print("You won!\n")
else:
    print("You lose.\n")
