import random
import time

# Function to introduce the game and initialize game setup.
def intro(HighScore):
    print("=================================\nWELCOME TO MY FIRST GAME OF MEMORY CARDS\n=================================")
    time.sleep(0.5)
    print("You have 8 CARDS and you  must find all the 4 identical cars!\n=================================")
    time.sleep(0.5)
    startingCards(HighScore)            # Move to startingCards to create the list which the player will see

# Function to shuffle the cards randomly.
def randomize(HighScore):
    random.shuffle(list)                # Shuffling the numbers in the list
    if HighScore != 999:                # If the high score isn't 999, the player already played at least once
        startingCards(HighScore)

# Function to display the initial set of cards.
def startingCards(HighScore):
    list_index = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]"] # Create the list the player will see
    print("\n=================================\n" + "These are your CARDS!", end=" ")
    time.sleep(0.5)
    for elem in list_index:
        print(elem, end=" ")           # Print the list to the player
        time.sleep(0.2)
    time.sleep(0.5)
    playTime(HighScore, list_index)    # Move to PlayTime to start the game

# Function to play the game.
def playTime(HighScore, list_index):
    Tries = 0                           # Initialize player tries
    conditionWinList = list[:]          # Update the winning list with the current shuffled list
    ReadyToPlay = True                  # Check with the while loop if the player is ready to play
    while ReadyToPlay:
        play = input("\n=================================\nAre you ready to play? (Y/N):")
        if play.lower() == "y":
            ReadyToPlay = False         # Change ReadyToPlay to False to exit the loop after the if statement
            time.sleep(0.5)
            win = False                 # Initialize win variable to check later if the player wants to play again
            while not win:              # Continue looping until the player wins
                print("\n=================================\nFrom your cards, select a card to see its hidden number\n=================================\n")
                selected_card1 = int(input("Select card(1-8): "))   # Player's first card selection
                while selected_card1 < 1 or selected_card1 > 8:     # Validate the input
                    print("\nInvalid Card Number. Please select between 1-8")
                    selected_card1 = int(input("\nSelect card(1-8): "))
                temphold_index1 = list_index[selected_card1-1]      # Temporary holding the element from list_index
                temphold_number1 = list[selected_card1-1]           # Temporary holding the element from the list
                list_index.pop(selected_card1-1)                    # Delete the element from list_index
                list_index.insert(selected_card1-1, list[selected_card1-1])  # Add element from the list to list_index
                time.sleep(0.2)
                print("\n=================================")
                for elem in list_index:
                    print(elem, end=" ")                           # Print the updated list to the player
                    time.sleep(0.2)
                print("\n=================================\nSelect another one\n=================================")
                selected_card2 = int(input("Select card: "))       # Player's second card selection
                while selected_card2 < 1 or selected_card2 > 8:    # Validate the input
                    print("Invalid Card Number. Please select between 1-8")
                    selected_card2 = int(input("Select card(1-8): "))
                temphold_index2 = list_index[selected_card2-1]      # Temporary holding the element from list_index
                temphold_number2 = list[selected_card2-1]           # Temporary holding the element from the list
                list_index.pop(selected_card2-1)                    # Delete the element from list_index
                list_index.insert(selected_card2-1, list[selected_card2-1])  # Add element from the list to list_index
                time.sleep(0.2)
                for elem in list_index:
                    print(elem, end=" ")                           # Print the updated list to the player
                    time.sleep(0.2)
                print("")

                if temphold_number1 != temphold_number2:            # Check if the player found two identical cards
                    list_index.pop(selected_card1-1)               # Reset to the previous list
                    list_index.insert(selected_card1-1, temphold_index1)
                    list_index.pop(selected_card2-1)
                    list_index.insert(selected_card2-1, temphold_index2)
                    time.sleep(0.4)
                    print("\n=================================Wrong Card=================================\n")
                    time.sleep(1)
                    Tries += 1
                    win = win_condition(win, conditionWinList, list_index)    # Check if the player won
                    if win:
                        print("It took you " + str(Tries) + " tries to win. Good Job!!")
                        HighScore = High(Tries, HighScore)          # Check if there is a new highscore
                        Replay(HighScore)                            # Check if the player wants to play again
                    print("CURRENT CARDS")
                    for elem in list_index:
                        print(elem, end=" ")                        # Print the current list to the player
                        time.sleep(0.1)
                else:
                    Tries += 1
                    win = win_condition(win, conditionWinList, list_index)    # Check if the player won
                    if win:
                        print("It took you " + str(Tries) + " tries to win. Good Job!!")
                        HighScore = High(Tries, HighScore)          # Check if there is a new highscore
                        Replay(HighScore)                            # Check if the player wants to play again
                    print("CURRENT CARDS")
                    for elem in list_index:
                        print(elem, end=" ")                        # Print the current list to the player
                        time.sleep(0.1)
        elif play.lower() == "n":
            print("Thank you for playing my game!")
            ReadyToPlay = False
        else:
            print("That's not an acceptable letter. Please write 'Y' for Yes or 'N' for No:")

# Function to check if the player won.
def win_condition(Win, conditionWinList, list_index):
    if list_index != conditionWinList:       # Compare the existing list with the winning list
        return Win
    else:
        Win = True                           # Change win variable to True to leave the loop in playTime
        return Win

# Function to check for a new high score.
def High(tries, HighScore):
    if tries < HighScore:                    # Check to change the Highscore
        HighScore = tries
        print("NEW HIGH SCORE! =", HighScore)
        return HighScore
    else:
        return HighScore

# Function to ask the player if they want to play again.
def Replay(HighScore):
    replay = input("Would you like to play again? (Y/N): ")
    if replay.lower() != "y":               # Check if the player wants to play again
        return "didn't want to play again"  # If they don't want to play, quit the program
    else:
        randomize(HighScore)                # If they want to play, create a new list

# Main Program
list = [1, 1, 2, 2, 3, 3, 4, 4]            # Create the list with the numbers we'll have in the game
list_index = ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]"] # Create the list that the player will see
conditionWinList = []                       # Create the winning list that list_index will be compared to later
HighScore = 999
randomize(HighScore)                        # Shuffle the numbers in the list
intro(HighScore)                            # Start the game
