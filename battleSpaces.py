#Battle Spaces
from random import randint
player_board = ['_'] * 5
cpu_board = ['_'] * 5
piece = 'x'
print("""
Welcome To My Battle Spaces Game. The Goal Is To Guess The Location
Of The Opponent 3 Times. Whoever Reaches The Goal First,
That Player Is The Winner. Both Sides Are Given Spaces.
""")
def playerPieces():
    player_move = int(input('0-4 To Choose Your Starting Space On The Board: ')) #This is just extra code for me incase I got stuck.
    game_board[player_move] = piece
    cpu_move = randint(0,4)
    print('User Board:',game_board)
    
def battleSpaces():
    hits = 0
    cpu_hits = 0
    
    while True:
        cpu_move = randint(0,4)
        cpu_board = ['_'] * 5 #Everytime the loop restarts, a new board is created to replace the player pieces.
        cpu_board[cpu_move] = piece
        print("CPU Has Chose It's Position.".center(35,'='))
        player_move = int(input('Enter 0-4 To Send An Attack: '))
        player_board = ['_'] * 5 #New Board
        player_board[player_move] = piece
        print(player_board)
        if player_move == cpu_move:
            cpu_hits += 1
            print('CPU Hits:',cpu_hits)
            print('Good Job, Hit!!!') #If the player hits the cpu, the cpu takes damage.
        elif player_board != player_move:
            print('Miss, CPU Is Making A Move.'.center(35,'=')) # This happens if the player miss.
            cpu_move = randint(0,4)
            cpu_board = ['_'] * 5 #New Board
            cpu_board[cpu_move] = piece
            player_board = ['_'] * 5 #New Board
            player_move = int(input('0-4 Chose A Position To Avoid The Attack: '))
            player_board[player_move] = piece
            print(player_board)
            if cpu_move == player_move: #Player gets a hit instead
                hits += 1
                print('Player Has Been Hit!!!'.center(35,'='))
                print('Player Hits:',hits)
                continue
            elif cpu_move != player_move: #Both Parties Missed
                print('Miss, Both Parties Regroup.'.center(35,'='))
                continue
            
        if cpu_hits == 3:
            print('Player Has Beat The CPU!!!!')
            break
        if hits == 3:
            print('The CPU Has Beat The Player!!!!')
            break
            

battleSpaces()
