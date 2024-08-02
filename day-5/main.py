"""
Day 5 - Guess The Number
"""

import random


def main():
    secret = random.randint(1, 50)
    turn = 10

    print("Welcome to Guess The Number!")
    print("I have selected one random number from 1 - 50.")
    print(f"You have {turn} turn for guess the number")

    while turn > 0:
        answer = int(input("Enter your answer: "))

        if answer < secret:
            print("The number is too small.")
        elif answer > secret:
            print("The number is too big.")
        else:
            print(
                f"Congratulations! You guess the right number. The right number is {secret}."
            )
            break

        turn -= 1
        print(f"Your turn: {turn}")

    if turn == 0:
        print(f"Sorry, you dont have a turn. The right number is {secret}.")


if __name__ == "__main__":
    main()
