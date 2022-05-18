# Write your solution here
def who_won(game_board:list):
    count = 0
    count_two =0
    
    for row in game_board:
        for item in row:
            if item == 1:
                count +=1
            if item == 2:
                count_two +=1
          
                

    if count > count_two:
        return 1, print("Player 1 wins") #player 1 won
    elif count_two > count:
        return 2, print("Player 2 wins") #player 2 won
    else:
        return 0, print("Nobody won") #nobody won

if __name__ == "__main__":
    who_won([[1,2,0],[1,2,0,1]])