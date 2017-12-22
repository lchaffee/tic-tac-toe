
# coding: utf-8

# In[1]:


from IPython.display import clear_output
def display_board(board):
    
    clear_output()
    print('  |   |')
    print(' ' +board[7] + ' | ' +board[8] + ' | ' + board[9])
    print('  |   |')
    print('----------')
    print('  |   |')
    print(' ' +board[4] + ' | ' +board[5] + ' | ' + board[6])
    print('  |   |')
    print('----------')
    print('  |   |')
    print(' ' +board[1] + ' | ' +board[2] + ' | ' + board[3])
    print('  |   |')


# In[2]:


def player_input():
    
    marker=''
    while not (marker=='X' or marker=='0'):
        marker=input('Player 1: Do you want to be X or 0?')
        
        if marker=='X':
            return('X','0')
        else:
            return('0','X')


# In[3]:


def place_marker(board,marker,posistion):
    board[posistion]=marker


# In[4]:


def win_check(board,mark):
    
    return ((board[7]==mark and board[8]==mark and board[9]==mark)#across top
    
           (board[4]==mark and board[5]==mark and board[6]==mark)#across middle
           (board[1]==mark and board[2]==mark and board[3]==mark)#across bottom
           (board[7]==mark and board[4]==mark and board[1]==mark)#down the left
           (board[8]==mark and board[5]==mark and board[2]==mark)#down middle
           (board[9]==mark and board[6]==mark and board[3]==mark)#down the righd
           (board[7]==mark and board[5]==mark and board[3]==mark)#diagonal
           (board[9]==mark and board[5]==mark and board[1]==mark))#diagonal


# In[5]:


import random 
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[6]:


def space_check(board, position):
    
    return board[position]==''


# In[7]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[8]:


def player_choice(board):
    #using strings because of raw_input
    position =' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        position=input('choose your next position:(1-9) ')
    return int(position)


# In[9]:


def replay():
    
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startwith('y')


# In[ ]:


print('Welcom to Tic Tac Toe!')

while True:
    #reset the board
    theBoard=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' Will go first.')
    game_on=True
    
    while game_on:
        if turn=='Player 1':
            #player1's turn
            
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn='Player 2'
    else:
        #player2's turn
        
        display_board(theBoard)
        position=player_choice(theBoard)
        place_marker(theBoard,player2_marker,position)
        
        if win_check(theBoard,player2_marker):
            display_board(theBoard)
            print('Player 2 has won!')
            game_on=False
        else:
            if full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                break
            else:turn='Player 1'
                
    if not replay():
        break

