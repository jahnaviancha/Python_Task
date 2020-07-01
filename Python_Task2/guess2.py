# Modify the program so that it asks users whether they want to guess again each time.
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question of whether they want to continue guessing.
# The program stops if the user guesses the correct number or answers “no”.
# ( The program continues as long as a user has not answered “no” and has not guessed the correct number)


lucky_number=10
guess_number=int(input("Try to guess the lucky number:"))
while guess_number != lucky_number:
    print("You guess wrong number")
    answer=input("You would like to continue please select your option yes/no:")
    if answer == 'no':
        break
    elif answer == 'yes':
        guess_number=int(input("guess again :"))
if guess_number == lucky_number:
    print("Your guess is correct", guess_number)
