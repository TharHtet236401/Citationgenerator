import random;

cards = [ 11, 2,3,4,5,6,7,8,9,10,10,10,10]

randomNumber = random.choice(cards)


    
player = []
playerCount = 0
computer = []
computerCount = 0

for i in range(0,2):
    randomNumber = random.choice(cards)
    player.append(randomNumber)
    while (playerCount > 21 and player[i] == 11):
        player[i]= 1
    playerCount += player[i]
    
for j in range (0,2):
     randomNumber = random.choice(cards)
     computer.append(randomNumber)
     while (computerCount > 21 and player[j] == 11):
        player[j]= 1
     computerCount += computer[j]
    
while (computerCount< 17):
    randomNumber = random.choice(cards)
    computer.append(randomNumber)
    computerCount += computer[len(computer)-1]
    
    
    
        
print (player, playerCount)
print (computer , computerCount)

print ("This is the start of the BlackJackGame")


print ("These are your card", player)
print ("This is computer frist Card ", computer[0])
decision = input("Would you like to draw one more card? y or n?")
while (decision == "y"):
    decision = input("Would you like to draw one more card? y or n?")
    while(decision == "y"):
        randomNumber = random.choice(cards)
        player.append(randomNumber)
        while (playerCount > 21 and randomNumber == 11):
            randomNumber = 1
            playerCount += randomNumber
            if (playerCount > 21):
                break
                
        print (player, playerCount)
        

