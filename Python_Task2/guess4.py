lucky_number = 25
counter = 1
while counter <= 5:
    guess_number=int(input("Guess the number : "))
    counter = counter + 1
    if guess_number == lucky_number:
        print("Good Guess")
        break
    else:
        print("Try Again")
if guess_number != lucky_number:
    print("Sorry but that wasn't very successful")
