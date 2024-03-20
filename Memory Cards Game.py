
import random
import time

def intro(HighScore):
    print("=================================\nWELCOME TO MY FIRST GAME OF MEMORY CARDS\n=================================")
    time.sleep(0.5)
    print("You have 8 CARDS and you  must find all the 4 identical cars!\n=================================")
    time.sleep(0.5)
    startingCards(HighScore)            #Moving to def startingCards to create the list which the player will see (list_index)





def randomize(HighScore):
    random.shuffle(list)                #Shuffling the numbers in the list
    if HighScore != 999:                  #If the highscore isn't 999 it means the player already played at least once.
        startingCards(HighScore)





def startingCards(HighScore):
    list_index = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]",] #Creating the list the player will see
    print("\n=================================\n" + "These are your CARDS!",end=" ")
    time.sleep(0.5)
    for elem in list_index:
        print (elem,end=" ")            #Printing the list to the player
        time.sleep(0.2)
    time.sleep(0.5)
    playTime(HighScore,list_index)                 #Moving to def PlayTime to start the game





def playTime(HighScore,list_index):
    Tries = 0                               #Initial Value for player tries.              
    conditionWinList = list[:]              #Updating the winning list with the current shuffled list.
    ReadyToPlay = True                      #Initializing to check with the while loop if the player is ready to play.
    while ReadyToPlay:
        play = input("\n=================================\nAre you ready to play? (Y/N):")
        if play.lower() == "y":             #Checking what the player typed and using the .lower method for practicality
            ReadyToPlay = False             #Changing ReadyToPlay to False so that we can exit the while loop after the if statement
            time.sleep(0.5)
            win = False                     #Initializing win variable to check later on if the player wants to play again
            while not win:                  #While it's false keep looping
                print("\n=================================\nFrom you cards please select a card to see its' hidden number\n=================================\n")
                selected_card1 = int(input("Select card(1-8): "))           #Card Selection from Player
                while selected_card1 < 1 or selected_card1 > 8:             #Validy Check for the above input.
                    print("\nInvalid Card Number. Please select between 1-8")        
                    selected_card1 = int(input("\nSelect card(1-8): "))         
                temphold_index1 = list_index[selected_card1-1]              #Temporary holding the element from the list (list_index)
                temphold_number1 = list[selected_card1-1]                   #Temporary holding the element for the list (list)
                list_index.pop(selected_card1-1)                            #Deleting the element with position(selected_card-1) from the list (list_index)**The list the player sees
                list_index.insert(selected_card1-1,list[selected_card1-1])  #Adding element with position(selected_card-1 from the list(list) to the list(list_index))
                time.sleep(0.2)         
                print("\n=================================")                                    
                for elem in list_index:                     
                    print (elem,end=" ")                                    #Printing the updated list (list_index) to the player
                    time.sleep(0.2)                       
                
                print("\n=================================\nSelect another one \n=================================")
                selected_card2 = int(input("Select card: "))                #2nd Card Selection from Player
                while selected_card2 < 1 or selected_card2 > 8:             #Validy Check for the above input.
                    print("Invalid Card Number. Please select between 1-8")        
                    selected_card2 = int(input("Select card(1-8): ")) 
                temphold_index2 = list_index[selected_card2-1]              #Temporary holding the element from the list (list_index)
                temphold_number2 = list[selected_card2-1]                   #Temporary holding the element for the list (list)
                list_index.pop(selected_card2-1)                            #Deleting the element with position(selected_card2-1) from the list (list_index)**The list the player sees
                list_index.insert(selected_card2-1,list[selected_card2-1])  #Adding element with position(selected_card2-1 from the list(list) to the list(list_index))
                time.sleep(0.2)                                             
                for elem in list_index:
                    print (elem,end=" ")                                    #Printing the updated list (list_index) to the player
                    time.sleep(0.2)
                print("")

                if temphold_number1 != temphold_number2:                    #Checking if the player found two identical cards
                    list_index.pop(selected_card1-1)                                #
                    list_index.insert(selected_card1-1,temphold_index1)             #
                                                                                    #Reseting to the previous list
                    list_index.pop(selected_card2-1)                                #
                    list_index.insert(selected_card2-1, temphold_index2)            #
                    time.sleep(0.4)
                    print("\n=================================Wrong Card=================================\n")
                    time.sleep(1)
                    Tries += 1
                    win = win_condition(win,conditionWinList,list_index)                   #Going to def win to check if the player won
                    if win:
                        print("It took you " + str(Tries) + " tries to win. Good Job!!")
                        HighScore = High(Tries,HighScore)                                   #Going to def High to check if there is a new highscore
                        Replay(HighScore)                                                #Going to def Replay to check if the player wants to play again
                    print("CURRENT CARDS")
                    for elem in list_index:
                        print (elem,end=" ")                                #Printing the current list to the player
                        time.sleep(0.1)
                else:
                    Tries += 1
                    win = win_condition(win,conditionWinList,list_index)                   #Going to def win to check if the player won
                    if win:
                        print("It took you " + str(Tries) + " tries to win. Good Job!!")
                        HighScore = High(Tries,HighScore)                                   #Going to def High to check if there is a new highscore
                        Replay(HighScore)                                                #Going to def Replay to check if the player wants to play again
                    print("CURRENT CARDS")
                    for elem in list_index:
                        print (elem,end=" ")                                #Printing the current list to the player
                        time.sleep(0.1)
        elif play.lower() == "n":
            print("Thank you for playing my game!")
            ReadyToPlay = False
        else:
            print("That's not an acceptable letter. Please write 'Y' for Yes or 'N' for No:")


        
              
def win_condition(Win,conditionWinList,list_index):
    if list_index != conditionWinList:                       #Comparing the existing list with the list that wins the game
        return Win
    else:
        Win = True                  #If they are the same, change win variable to true so that it leaves from the loop in def playTime
        return Win
    



        
def High(tries,HighScore):
    if tries < HighScore:                               #Checking to change the Highscore
        HighScore = tries
        print("NEW HIGH SCORE!",end=" = ")
        print(HighScore)
        return HighScore
    else:
        return HighScore
    



def Replay(HighScore):
    replay = input("Would you like to play again? (Y/N): ")
    if replay.lower() != "y":                               #Checking if the player wants to play again
        return "didnt want to play again"                                 #If he doesn't want to play the programm quits
    else:                                                   #
        randomize(HighScore)                                #If he want to play we are going to def randomize to create a new list




#Main Programm
list = [1,1,2,2,3,3,4,4]           #Creating the list with the numbers we'll have in the game
list_index = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]",] #Creating the list that the player will see
conditionWinList = []                                           #Creating the wining list that the list_index will be compared to later on
HighScore = 999
randomize(HighScore)                #Going to def randomize to shuffle the numbers in the list (list)
intro(HighScore)                    #Going to def intro to start the game

        