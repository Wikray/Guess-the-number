import random

CEND      = '\33[0m'
CVIOLET = '\33[35m'
CRED    = '\33[31m'
CGREEN2  = '\33[92m'
CBLUE   = '\33[34m'

secret_Number = random.randint(1, 100000)
guess = -1
counter = 0

while guess != secret_Number:
    guess = int(input(CBLUE + "Type in your guess: " + CEND))

    if guess < secret_Number:
        print("Your guess is too " + CRED +"low!" + CEND)

    if guess > secret_Number:
        print("Your guess is too " + CRED + "high!" + CEND)

    counter = counter + 1

print(CBLUE + "Congratulations, you guessed the number " + CVIOLET + str(secret_Number) + CBLUE + " in " + CBLUE + str(counter) + " try/s")

