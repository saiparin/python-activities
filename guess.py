import random
playing=True
number=str(random.randint(0,9))
print("i will generate a number between 0 and 9, and guess the number to end the game.")
print("keep guessing till you get the number right")
while playing:
    guess=input("number of your choice:")
    if number==guess:
        print("win the game")
        print("the number was",number)
        break
    else:
        print("try again")