import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter Number between 1 ~ {x} :"))
        if guess < random_number:
            print("sorry, guess again . Too low .")
        elif guess > random_number:
            print("sorry, guess again . Too High .")

    print(f"you have gusee the number :  {random_number} . Correct Answer")


def Computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"its {guess} Too high (H) . Too Low (L) . Correct (C)  ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"yay , the computer guess your number , {guess} , Correct")


Computer_guess(1000)


# Guess Number Secand App with Kily 💓
