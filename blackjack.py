

import random



# choose the card from the array of cards;
def dealCard():
    cards = [ 11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calScore(card):
  
    if sum(card) == 21 and len(card)==2:
        return 0
    
    if 11 in card and sum(card)>21 :
        card.remove(11)
        card.append(1)
    
    return sum (card)
        
def compare (userScore, computerScore):
    if (userScore == computerScore):
        print("Draw")
    elif (userScore == 0):
        print("You Winn")
    elif (computerScore == 0):
        print("You Lost")
    elif (computer_card > 21 ):
        print(" Opponent went over , you win")
    elif( user_card > 21):
        print (" you went over , you lost ")
    elif (userScore > computerScore):
        print ("You winn")
    else:
        print ("You lost ")

playAgain = "y"
while (playAgain == "y"):
    user_card = []
    computer_card = []
    
    is_game_over = False

    for i in range (2):
        user_card.append(dealCard())
        computer_card.append(dealCard())
        
    while not is_game_over:
        
        userScore = calScore(user_card)
        computerScore = calScore(computer_card)
        
        print (f" The user card are {user_card} and the current score is {userScore}")
        print (f"The computer card is {computer_card}")

        if userScore == 0 or computerScore == 0 or userScore> 21:
            is_game_over= True
        else:
            deal_or_not = input("Do you want one more card or not : y or n ")
            if deal_or_not == "y":
                user_card.append(dealCard())
                userScore = calScore(user_card)
            else:
                is_game_over= True
            
    while (computerScore < 17 and computerScore !=0 ):
        computer_card.append(dealCard())
        computerScore = calScore(computer_card)
    
    print (f" The user card are {user_card} and the final score is {userScore}")
    print (f"The computer card is {computer_card} and the final score is {computerScore}")  

    compare(userScore, computerScore)
    
    playAgain = input("play againg : y or n")



    


    