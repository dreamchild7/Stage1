import random

number = random.randint(1, 9)

count = 0

guess = int(input("Enter a number between 1 and 9:"))

while count < 5;

    if guess == number:
        print("You entered a correct number")
        break
    elif guess < number:
        print("Your number is lower than 1")

    else:
        print("Your number is higher than 9")

        count += 1

    if not count < 5:
        print("Your number is not correct")
        
        
