class ChessPieces:
	def __init__(self, array):
		self.king = []
		self.pieces = []
		self.board_size = len(array)

def checkmate(board):
	try:
		array = board.split()
		if board.count("K") != 1:
			return print("Error!")
		for row in array:
			if len(row) != len(array):
				return

		Chess = ChessPieces(array)
		for row in range(len(array)):
			for col in range(len(array[0])):
				if array[row][col] == "K":
					Chess.king = [row, col]
				elif array[row][col] in ["P", "R", "B", "Q"]:
					Chess.pieces.append([row, col])
		
		if check_all(array, Chess) == True:
			print("Success")
		else:
			print("Fail")
	except:
		 print("Error with exception")

def check_all(array, Chess):
	for row in range(len(array)):
		for col in range(len(array[0])):
			if array[row][col] == "P":
				if check_pawns(Chess, row, col) == True:
					return True
			elif array[row][col] == "R":
				if check_rooks(Chess, row, col) == True:
					return True
			elif array[row][col] == "B":
				if check_bishops(Chess, row, col) == True:
					return True
			elif array[row][col] == "Q":
				if check_queens(Chess, row, col) == True:
					return True

#	X.X
#	.P.
#	...
def check_pawns(Chess, row, col):
	if [row - 1, col - 1] == Chess.king:
			return True
	elif [row - 1, col + 1] == Chess.king:
			return True

#	.|.
#	-R-
#	.|.
def check_rooks(Chess, row, col):
	for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
		if walk_to_king(direction[0], direction[1], Chess, row, col) == True:
			return True

#	\./
#	.B.
#	/.\
def check_bishops(Chess, row, col):
	for direction in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
		if walk_to_king(direction[0], direction[1], Chess, row, col) == True:
			return True

#	\|/
#	-Q-
#	/|\
def check_queens(Chess, row, col):
	if check_rooks(Chess, row, col) == True:
		return True
	elif check_bishops(Chess, row, col) == True:
		return True

#	Q..
#	.\.
#	..K
def walk_to_king(dir_row, dir_col, Chess, row, col):
	step = 1
	while step < Chess.board_size:
		move_row = row + (dir_row * step)
		move_col = col + (dir_col * step)
		if [move_row, move_col] == Chess.king:
			return True
		elif [move_row, move_col] in Chess.pieces:
			return False
		step = step + 1
	return False