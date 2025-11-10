theBoard={'7': ' ' , '8': ' ', '9': ' ',
          '4': ' ' , '5': ' ', '6': ' ',
          '1': ' ' , '2': ' ', '3': ' ',}

board_keys=[]

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game 
    and thus we will make function in which we'll define the printBoard 
    function so that we can easily print the board everytime by calling this function.'''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' board['3'])

 #Now we'll write the main function which has all the gameplay functionality.

def game():

    turn='X'
    count='0'

    for i in range(10):
        printBoard(theBoard)
        print("Its your turn," + turn + ". Move to which place?")
        move=input()
        if theBoard[move]==' ':
            theBoard[move]=turn
            count+=1
        else:
            print("That place is already filled.\n Move to which place?")
            continue
        #Now we will check if player X or O has won, for every move after 5 moves.

        if count>=5:
            if theBoard['7']==theBoard['8']==theBoard['9'] != ' ':
                #Across the top
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn+"Won. **** ")
                break   
                 #Across the middle
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn+"Won. **** ")
                break
            elif theBoard['1']==theBoard['2']==theBoard['3'] != ' ':
        #Across the bottom
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn+"Won. **** ")
                break
            elif theBoard['1']==theBoard['4']==theBoard['7'] != ' ':
        #Down the left side
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn+"Won. **** ")
                break
            elif theBoard['2']==theBoard['5']==theBoard['8'] != ' ':
        #Down the middle
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn+"Won. **** ")
                break
            elif theBoard['3']==theBoard['6']==theBoard['9'] != ' ':
        #Down the right side
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn+"Won. **** ")
                break
            elif theBoard['7']==theBoard['5']==theBoard['3'] != ' ':
        #Diagonal
                printBoard(theBoard)
                print("\n Game Over. \n")
                print(" **** " +turn+"Won. **** ")
                break
            elif theBoard['1']==theBoard['5']==theBoard['9'] != ' ':
        #Diagonal
                printBoard(theBoard)
                print("\n Game Over. \n")
            print(" **** " +turn+"Won. **** ")
            break
    
    #If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count==9:
        print("\nGame Over.\n")
        print("It's a Tie!!")

        #Now we have to change the player after every move.
        if turn=='X':
           turn='O'
        else:
            turn='X'

    #Now we will ask if player wants to restart the game or not.
    restart=input("Do you want play again?(y/n)")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            theBoard[key]=" "
        
        game()

if __name__== "__main__":
    game()

