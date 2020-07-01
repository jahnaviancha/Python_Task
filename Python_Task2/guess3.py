lucky_number = 25
counter=1

while counter <= 5:
    guess_number = int(input("Try to guess the lucky number :"))
    counter = counter + 1
    if guess_number == lucky_number:
        print("Good Guess")
    else:
        print("Try Again")
print("Game Over!")

