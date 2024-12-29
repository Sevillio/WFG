from random import randint

# create a list of play options
t =['Water', 'Fire', 'Grass']

#assign a random play to the computer 
computer = t[randint(0,2)]

#set the player to False
player = False

#set game to False 
game = False 

#Score and turns
score = 0
computerscore = 0
finalscore = 3
turn = 0
max_turn = 5 


while not game:
    computer = t[randint(0, 2)] 

    while not player  :
        #set player to True 
            player =  input("Water Fire, Grass?").capitalize()
            if player == computer:
                print("Tie")
                player = False
                print(f"Player Score: {score}, Computer Score: {computerscore}, Turn: {turn}")
            elif player =="Water":
                if computer =="Grass":
                    print("You lose!", computer, "drains", player)
                    computerscore= computerscore +1
                    print("computerscore:",computerscore)
                    player = False
                    turn = turn+1
                    print(f"Player Score: {score}, Computer Score: {computerscore}, Turn: {turn}")
                else:
                    print("You win!", player, "extinguish",computer)
                    score = score +1
                    print("playerscore: ", score)
                    player = False
                    turn = turn+1
                    print(f"Player Score: {score}, Computer Score: {computerscore}, Turn: {turn}")
            elif player =="Fire":
                if computer =="Water":
                    print("You lose", computer, "extinguise", player)
                    computerscore= computerscore +1
                    print("computerscore: ", computerscore)
                    player = False
                    turn = turn+1
                    print(f"Player Score: {score}, Computer Score: {computerscore}, Turn: {turn}")
                else:
                    print("You win", player, "burned", computer)
                    score = score +1
                    player = False
                    turn = turn+1
                    print(f"Player Score: {score}, Computer Score: {computerscore}, Turn: {turn}")
            elif player =="Grass":
                if computer=="Fire":
                    print("You lose", computer, 'burns', player)
                    computerscore= computerscore +1
                    print("computerscore: ", computerscore)
                    player = False
                    turn = turn+1
                    print(f"Player Score: {score}, Computer Score: {computerscore}, Turn: {turn}")
                else:
                    print("You Win ", player, "absorb", computer)
                    score = score +1
                    print("playerscore: ", score)
                    player = False
                    turn = turn+1
                    print(f"Player Score: {score}, Computer Score: {computerscore}, Turn: {turn}")
            else:
                print("There is no winner. Try another move.")
                player = False
                turn = turn+1
                print(f"Player Score: {score}, Computer Score: {computerscore}, Turn: {turn}")
            #Code below check the following scenario's to end the game
            if turn >= max_turn:
                 game = True 
                 break
            elif score == finalscore:
                print("Game is over. Player wins!")
                game == True
                break
            elif computerscore == finalscore:
                print("Game is over. Computer wins!")
                game == True
                break


    
