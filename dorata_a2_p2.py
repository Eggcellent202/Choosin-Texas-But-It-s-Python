#Lucas Dorata
#assignment 2
#Factoring numbers

nummbber = input("Input a random positive number between 1 to 10000: ")
#check to see if the input is a number
while nummbber.isnumeric() == False:
    print("That is not a valid integer. Please try again.")
    nummbber = input("Input a random positive number between 1 to 10000: ")

castNum = int(nummbber)

#check to see if the number is between 1 - 10000
while castNum <= 0 or castNum > 10000:
    print("Please input an integer between 1 to 10000. Please try again.")
    castNum = int(input("Input a random positive number between 1 to 10000: "))

#checks every number to see if it is divisible by tractorsF
checkFactor = 1
tractorsF = []
while checkFactor <= castNum:
    #check if castNum is divisible by checkFactor
    if castNum % checkFactor == 0:
        tractorsF.append(checkFactor)
    checkFactor += 1

countF = len(tractorsF)
print(f"Found {countF} factor(s) for your number: {castNum}.")
if countF == 2:
    print("The number is prime.")

listOfFactor = input("Do you want to show the list of factors? Type Y or hit enter if yes or N for no: ").lower()

while listOfFactor != "y" and listOfFactor != "n" and listOfFactor != "":
    listOfFactor = input("Please hit enter or Y or N: ").lower()

if listOfFactor == "y" or listOfFactor == "":
    print(f"This is the full list of factors for your number: {tractorsF}")

#print("Thanks for using my super calculator.")
