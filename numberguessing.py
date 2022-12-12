import random

num = random.randint(1, 10)

guess = int(input("Can you guess the number between 1 to 10?:\n"))
count =0

while count < 5:
    count += 1
    if guess == num:
        print("You guessed the number in " + str(count) + " attempts")
        break
    elif guess > num:
        guess = int(input("Your guess is too high:\n"))
    elif guess < num:
        guess = int(input("Your guess is too low:\n"))

if count >= 5:
    print("The Number of attempts exceeded 5 times, please try next time")
