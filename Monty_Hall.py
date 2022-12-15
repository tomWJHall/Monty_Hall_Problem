import random as rd

lists = [[True, False, False], [False, True, False], [False, False, True]]
#Creating the list of the different configurations behind the doors

def monty():
    
    successIndex = rd.randint(0, 2)
    successList = lists[successIndex]
    #Randomly choosing the configuration.
  
    listDisplay = ["🚪"]*3
    print(listDisplay, end='\n\n')
    #Creating the list to display to the user.
  
    print("Select door number (between 1, 2 or 3): ", end='\n\n')
    inputIndex = int(input()) - 1
    
    if(not(inputIndex in [0, 1, 2])):
        print("Incorrect input. Try Again: ", end='\n\n')
        monty()
        
    print("You chose: ", inputIndex + 1, end='\n\n')
    #Asking the user to choose the door they think has a car behind it.


    remainList = [0, 1, 2]
    remainList.remove(successIndex)
    
    if(inputIndex != successIndex):
        remainList.remove(inputIndex)

    #remainList is the list from which the program chooses to display a duck.

    
    displayIndex = rd.choice(remainList)
    listDisplay[displayIndex] = "🦆"
    print(listDisplay, end='\n\n')
    #Opening a first door with a duck behind it.

    
    choiceList = [0, 1, 2]
    choiceList.remove(displayIndex)
    #choiceList is the list from which the user decides to keep their choice or change it.
    #It only contains the chosen door and the other door with a duck behind it.
    
    remainList = [0, 1, 2]
    remainList.remove(displayIndex)
    #remainList now contains the same as choiceList.
    
    choiceList.remove(inputIndex)
    #Now choicList is left with the door that wasn't initially chosen and that wasn't opened yet.

    
    print("Do you want to stick to your original choice (", inputIndex + 1, ") or go for the other one (", choiceList[0] + 1, ")?")
    
    inputIndex = int(input()) - 1
    
    while(not(inputIndex in remainList)):
        print("Incorrect input. Try Again: ")
        inputIndex = int(input()) - 1

    #Asking the user to choose (again) the door they think has a car behind it.

    listDisplay = ["🏎️" if(successList[0]) else "🦆",
                   "🏎️" if(successList[1]) else "🦆",
                   "🏎️" if(successList[2]) else "🦆"]

    #Updating the list to display
    
    
    if(successList[inputIndex]):
        print("Congratulations, you won!\n")
        print(listDisplay, end='\n')
    else:
        print("The door you chose wasn't the one. You failed, sorry.\n")
        print(listDisplay, end='\n')

    print('\n\n\n')
    #Finalising the game and opening all the door.

    monty()
    #Restarting the game.
    
monty()
#Calling the function.
