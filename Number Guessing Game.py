import random
print("\n<<< Guess The Number >>>\n")
print("<<< Choose Difficulty >>>")
mode = int(input("(1)Easy,(2)Medium, (3)Hard: "))
if mode == 1:
    AI = random.randrange(0,11)
    guess = int(input("Guess a number between 1 and 10: "))
    while guess != AI:
        if guess > AI:
            guess = int(input("Lower: "))
        elif guess < AI :
            guess = int(input("Higher: "))
    print("Your guess was right")

elif mode == 2:
    AI = random.randrange(0,51)
    guess = int(input("Guess a number between 1 and 50: "))
    while guess != AI:
        if guess > AI:
            guess = int(input("Lower: "))
        elif guess < AI :
            guess = int(input("Higher: "))
    print("Your guess was right")

elif mode == 3:
    AI = random.randrange(0,101)
    guess = int(input("Guess a number between 1 and 100: "))
    while guess != AI:
        if guess > AI:
            guess = int(input("Lower: "))
        elif guess < AI :
            guess = int(input("Higher: "))
    print("Your guess was right")