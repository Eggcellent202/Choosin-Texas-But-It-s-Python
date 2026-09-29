#Lucas Dorata
#assignment 2
#Guessing game 2 (The cool one)

#I was very familiar with these in my Java class
import random

#creates a random number between 0 - 100
randomNum = random.randint(0, 100)

guessessSoFar = []

#this is my absolute genius move that shatters the consept of basic understanding
i = 0
print("Guess a number between 0 and 100")
while True:
    guess = input("What is your first number guess? You can press q to give up: ")
    if guess.lower() == "q":
        print(f"You have quit the game. The number was {randomNum}")
        break

    while guess.isnumeric() == False:
        print("That is not a valid integer. Please try again.")
        guess = input("What is your first number guess? You can press q to give up: ")

        #First break is for the nested while loop, secound is for the big while loop
        if guess.lower() == "q":
            print(f"You have quit the game. The number was {randomNum}")
            i = 1
            break
    #the master at work
    if i == 1:
        break

    numGuess = int(guess)

    if numGuess in guessessSoFar:
        print("You already guessed that number")
    else:
        guessessSoFar.append(numGuess)

    if numGuess < randomNum:
        print("Too low")
    
    elif numGuess > randomNum:
        print("Too high")

    else:
        print(f"You got it! The number was {randomNum}")
        break
print("Thanks for playing!")