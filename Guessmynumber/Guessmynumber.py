import random

# computer's number
computersnumber = random.randint(1, 20)
print("I am thinking of a number between 1 - 20,")
print("Take a guess")

# number of guesses before they give up(6)


def runninggame():
    guesscounter = 0
    for myguesses in range(1, 7):
        myguess = int(input())
        guesscounter += 1
        print(f"number of tries: {guesscounter}")

        if myguess > computersnumber:
            print("Guess lower")
        elif myguess < computersnumber:
            print("Guess higher")
        elif myguess == computersnumber:
            print(f'you got it! the number was {computersnumber}')
            return
        if guesscounter == 6:
            print(
                f'Sorry, you used all your attempts. The number was {computersnumber}')


runninggame()