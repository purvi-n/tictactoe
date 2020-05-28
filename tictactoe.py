board=["-", "-", "-",
		"-", "-", "-",
		"-", "-", "-",]
gameOn=True
winner=None
currPlayer="X"

def dispBoard():
	print(board[0]+" | " + board[1]+" | "+ board[2])
	print(board[3]+" | " + board[4]+" | "+ board[5])
	print(board[6]+" | " + board[7]+" | "+ board[8])

def handleTurn(currPlayer):
	print("\n"+currPlayer+"'S TURN!")
	pos=input("Choose position from 1-9: ")
	valid = False
	while not valid:
		while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			pos=input("Invalid input! Choose position from 1-9: ")
		pos=int(pos)-1
		if board[pos]=="-":
			valid=True
		else:
			print("Can't put value there. GO AGAIN!")
	board[pos]=currPlayer
	print("\n")
	dispBoard()

def checkIfOver():
	checkIfWin()
	checkIfTie()

def checkRows():
	global gameOn
	row1=board[0]==board[1]==board[2]!="-"
	row2=board[3]==board[4]==board[5]!="-"
	row3=board[6]==board[7]==board[8]!="-"
	if row1 or row2 or row3:
		gameOn=False
	if row1:
		return board[0]
	elif row2:
		return board[3]
	elif row3:
		return board[6]
	return

def checkCols():
	global gameOn
	col1=board[0]==board[3]==board[6]!="-"
	col2=board[1]==board[4]==board[7]!="-"
	col3=board[2]==board[5]==board[8]!="-"
	if col1 or col2 or col3:
		gameOn=False
	if col1:
		return board[0]
	elif col2:
		return board[1]
	elif col3:
		return board[2]
	return

def checkDiags():
	global gameOn
	diag1=board[0]==board[4]==board[8]!="-"
	diag2=board[2]==board[4]==board[6]!="-"
	if diag1 or diag2:
		gameOn=False
	if diag1:
		return board[0]
	elif diag2:
		return board[2]
	return

def checkIfWin():
	global winner
	#check rows
	rowWinner=checkRows()
	#check cols
	colWinner=checkCols()
	#check diags
	diagWinner=checkDiags()
	if(rowWinner):
		winner=rowWinner
	elif(colWinner):
		winner=colWinner
	elif(diagWinner):
		winner=diagWinner
	else:
		winner=None
	return

def checkIfTie():
	global gameOn
	if "-" not in board:
		gameOn=False
	return

def flipPayer():
	global currPlayer
	if currPlayer=="X":
		currPlayer="O"
	else:
		currPlayer="X"
	return

def playGame():
	dispBoard()
	while gameOn:
		handleTurn(currPlayer)
		checkIfOver()
		flipPayer()
	#when game ends
	if(winner=="X" or winner=="O"):
		print("\n"+winner+" WON!")
	else:
		print("\n"+"TIE!")



#main
playGame()