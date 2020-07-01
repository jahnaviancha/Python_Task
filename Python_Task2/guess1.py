# Write a program such that it asks users to “guess the lucky number”.
# If the correct number is guessed the program stops, otherwise it continues forever.


guess_number = int(input("Try to guess the lucky number:"))
lucky_number = 10
while True:
    if guess_number != lucky_number:
        print("Your guess is wrong")
        guess_number = int(input("Try again :"))
    elif guess_number == lucky_number:
        print("Your guess is correct", lucky_number)
        break


