# This is a guessing game that allows a player to guess the age of 
# The writer of this code.

answer = int(input("Guess my age boy: "))
tries = 1
while tries < 4:
    if answer == 27:
        print(f"You are officially a wizard! {answer} years old is just right! You win.")
        break
    else:
        tries += 1
        print("Try again buddy.")
        answer = int(input("Guess my age again boy: "))
if answer == 27:
    print("Bye")
else:
    print("Gerrarahia mehn. You no sabi me.")