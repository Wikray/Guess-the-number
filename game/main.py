secret_Number = int(input("Type in the number your partner should guess: "))
guess = -1
counter = 0

while guess != secret_Number:
    guess = int(input("Type in your guess: "))

    if guess < secret_Number:
        print("Your guess is too low!")

    if guess > secret_Number:
        print("Your guess is too high!")

    counter = counter + 1

print("Congratulations, you guessed the number in" , counter, "trys")

