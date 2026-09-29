#Lucas Dorata
#assignment 2
#Choices

mainList = []
addingStr = input("Type a bunch of words with spaces between them: ")
#I googled .split(), 8/10 method
#.split() splits the list into individual strings.
mainList = addingStr.split()

countL = len(mainList)
print(f"You have entered {countL} words.")

#this adds a space. common in my Java class (highschool)
print("")

gloriousMenu = [ "1. Clear list",
                "2. Print list",
                "3. Alphabetize list",
                "4. Add word(s) to list", 
				"5. Delete word(s) from list", 
				"6. Remove duplicate words from list",
				"7. Exitprogram"
                ]

alphabetized = False
while True:
	#this kinda looks ugly but it works
	print("This is the glorious menu:")
	for choices in gloriousMenu:
		print(choices)
	choice = input("Enter the number from 1 - 7 of your choice: ")

	if choice == "1":
		confirmation = input("Are you sure you want to clear the list? Enter yes/no: ").lower()
		if confirmation == "yes":
			mainList.clear()
			print("You have cleared the list.")
		else:
			print("You have cancelled the list clear function.")
			
		#I added this line because I did not like how the menu would show up immediately after completing a choice
		continu = input("Press enter to continue")

    #this was the hardest one yet
	elif choice == "2":
		print(f"This is the current list: {mainList}")
		continu = input("Press enter to continue")
    
	elif choice == "3":
		#I googled .sort(), 9/10 method, it sorts the list alphabetically
		mainList.sort()
		#I googled alphabetized, 10/10 method, made me feel like and alpha 🐺
		alphabetized = True
		print("The list has been alphabetized.")
		continu = input("Press enter to continue")
		
	elif choice == "4":
		while True:
			awesomeNewStr = input("Enter some new word or words to your list: ")
			newNewWords = awesomeNewStr.split()
			if alphabetized == True:
				#🐺🐺🐺
				stayAlpha = input("The list is alphabetized. Do you want to keep it alphabetized? The new words will be added either way. yes/no?: ").lower()
				if stayAlpha == "yes":
					#I googled .extend(), it adds each word individually instead of nested like append
					mainList.extend(newNewWords)
					mainList.sort()
					print("The new words have been added to the list and re-alphabetized.")
				else:
					alphabetized = False
					print("The list is no longer alphabetized.")
					mainList.extend(newNewWords)
					print("The new words have been added to end of list.")
			else:
				mainList.extend(newNewWords)
				print("The new words have been added to the end of the list.")
			moreWords = input("Add more words? yes/no: ").lower()
			if moreWords == "no":
				break
			continu = input("Press enter to continue")

	elif choice == "5":
		print(f"This is the current list: {mainList}")
		deleteWords = input("Enter word(s) to delete: ")
		removedWords = []
		count = 0
		i = 0
		for i in deleteWords:
			#checks whether or not the word(s) is/are in main list
			wordCounter = mainList.count(deleteWords)
			#if there is the word in mainlist
			if wordCounter > 0:
				count += wordCounter
				removedWords.append(deleteWords)
				j = 0
				#if there are words in the list, repeat this task
				while j < wordCounter:
					if deleteWords in mainList:
						mainList.remove(deleteWords)
					j = j + 1
		print(f"{count} word(s) removed from the list.")
		more_info = input("Want more info? yes/no: ").lower()
		if more_info == "yes":
			print(f"Removed words: {removedWords}")
			continu = input("Press enter to continue")
		else:
			continu = input("Press enter to continue")

	elif choice == "6":
		print(f"This is the current list: {mainList}")
		confirmToSix = input("Are you sure you want to remove duplicates? Enter yes/no: ").lower()
		if confirmToSix == "yes":
			helpList = []
			#I found set() on google, 10/10 would try again. it removes duplicates from the list
			helpList = list(set(mainList))
			mainList = helpList
			print("Duplicate words removed.")
			continu = input("Press enter to continue")
		else:
			print("Duplicate removal cancelled.")
			continu = input("Press enter to continue")

	elif choice == "7":
		confirmToSeven = input("Are you sure you want to exit the program? Enter yes/no: ").lower()
		if confirmToSeven == "yes" or confirmToSeven == "y":
			print("Exiting the program.")
			break
		else:
			print("Exit cancelled.")
			continu = input("Press enter to continue")

	else:
		print("Invalid choice. Please enter a number from 1 to 7.")