board = [' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ' ]
turn = 'X'
cnt = 0
again=True

def printBoard(board):
	print('___________')
	print('   |   |   |')
	print(' ' + board[7]+ ' | ' + board[8] + ' | ' + board[9]+ ' | ')
	print('___|___|___|')
	print('   |   |   |')
	print(' ' + board[4]+ ' | ' + board[5] + ' | ' + board[6]+ ' | ')
	print('___|___|___|')
	print('   |   |   |')
	print(' ' + board[1]+ ' | ' + board[2] + ' | ' + board[3]+ ' | ')
	print('___|___|___|')


def insertWhere():
	global turn
	
	okay=True

	if(turn=='X'):
		while(okay):
			print()
			position=input('Player 1 insert your next position based on the numpad keyboard:')
			position=int(position)
			if(board[position]==' '): okay=False
			print()
	else:
		while(okay):
			print()
			position=input('Player 2 insert your next position based on the numpad keyboard:')
			position=int(position)
			if(board[position]==' '): okay=False
			print()

	board[position]=turn

	if(turn=='X'): turn='O' 
	else: turn='X'
		
	printBoard(board)

def winner():
	
	if(board[1]!=' ' and board[1]==board[2]==board[3]): return board[1]
	if(board[1]!=' ' and board[1]==board[4]==board[7]): return board[1]
	if(board[1]!=' ' and board[1]==board[5]==board[9]): return board[1]

	if(board[2]!=' ' and board[2]==board[5]==board[8]): return board[2]

	if(board[3]!=' ' and board[3]==board[5]==board[7]): return board[3]

	if(board[4]!=' ' and board[4]==board[5]==board[6]): return board[4]

	if(board[7]!=' ' and board[7]==board[8]==board[9]): return board[7]

	return '/'

def init():
	global turn

	turn = input("Player 1, choose your sign! If you choose 'O' you become Player 2:")
	
	while(turn!='X' and turn!='O'):
		turn = input("Player 1, choose your sign! If you choose 'O' you become Player 2:")


winnerCAR = '/'

init()
while(again==True):
	cnt=0
	while(winner()=='/'):
		insertWhere()
		if(winner()=='X'):
			print()
			print("Player 1 won!")
			winnerCAR = winner()
			break
		elif(winner()=='O'):
			print()
			print("Player 2 won!")
			winnerCAR = winner()
			break
		cnt+=1
		if(cnt==9):
			print()
			print("No winner!")
			print()
			break
		

	againn=input("If you want to play again, press Y. On the other hand, if you want to stop, press N:  ")
	if(againn=='N'):
		again=False
		print("Kraj!")
	else:
		for i in range(10):
			board[i]=' ' 
		printBoard(board)
		if(winnerCAR == 'X'): turn='O'
		elif (winnerCAR == 'O'): turn='X'
		else: turn = 'X'



