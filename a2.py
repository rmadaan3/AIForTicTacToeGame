#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.
We will estimate probability of winning for a player for different scenarios.
	 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
""" 
# There are 2 players: player1 and player2
# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2
# turn variable defines whose turn is now
#Player's no whose turn it is

def data():
	import tile
	tile.tile1= 0    
	tile.tile2= 0
	tile.tile3= 0
	tile.tile4= 0
	tile.tile5= 0
	tile.tile6= 0
	tile.tile7= 0
	tile.tile8= 0
	tile.tile9= 0
	tile.turn=tile.player1
	tile.move1=0
	tile.move2=0
	count=0

def validmove(move):
	
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	import tile
	if move==1 and tile.tile1==0:
		return True
	elif move==2 and tile.tile2==0:
		return True
	elif move==3 and tile.tile3==0:
		return True
	elif move==4 and tile.tile4==0:
		return True
	elif move==5 and tile.tile5==0:
		return True
	elif move==6 and tile.tile6==0:
		return True
	elif move==7 and tile.tile7==0:
		return True
	elif move==8 and tile.tile8==0:
		return True
	elif move==9 and tile.tile9==0:
		return True
	else:
		return False

def win():
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""
	import tile	
	if (tile.tile1==tile.tile2 and tile.tile2==tile.tile3 and tile.tile3==1) or (tile.tile4==tile.tile5 and tile.tile5==tile.tile6 and tile.tile6==1) or (tile.tile7==tile.tile8 and tile.tile8==tile.tile9 and tile.tile9==1) or (tile.tile1==tile.tile4 and tile.tile4==tile.tile7 and tile.tile7==1) or (tile.tile2==tile.tile5 and tile.tile5==tile.tile8 and tile.tile8==1) or (tile.tile3==tile.tile6 and tile.tile6==tile.tile9 and tile.tile9==1) or (tile.tile1==tile.tile5 and tile.tile5==tile.tile9 and tile.tile9==1) or (tile.tile3==tile.tile5 and tile.tile5==tile.tile7 and tile.tile7==1):
		return True
	elif (tile.tile1==tile.tile2 and tile.tile2==tile.tile3 and tile.tile3==2) or (tile.tile4==tile.tile5 and tile.tile5==tile.tile6 and tile.tile6==2) or (tile.tile7==tile.tile8 and tile.tile8==tile.tile9 and tile.tile9==2) or (tile.tile1==tile.tile4 and tile.tile4==tile.tile7 and tile.tile7==2) or (tile.tile2==tile.tile5 and tile.tile5==tile.tile8 and tile.tile8==2) or (tile.tile3==tile.tile6 and tile.tile6==tile.tile9 and tile.tile9==2) or (tile.tile1==tile.tile5 and tile.tile5==tile.tile9 and tile.tile9==2) or (tile.tile3==tile.tile5 and tile.tile5==tile.tile7 and tile.tile7==2):
		return True
	else:
		return False

def takeNaiveMove():
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""	
	from random import randint as randi
	import tile
	try:
		s=randi(1,9)
		if validmove(s):
			if s==1:
				tile.tile1=tile.turn
				return True
				#win()
			elif s==2:
				tile.tile2=tile.turn
				return True
				#win()
			elif s==3:
				tile.tile3=tile.turn
				return True
				#win()
			elif s==4:
				tile.tile4=tile.turn
				return True
				#win()	
			elif s==5:
				tile.tile5=tile.turn
				return True
				#win()
			elif s==6:
				tile.tile6=tile.turn
				return True
				#win()
			elif s==7:
				tile.tile7=tile.turn
				return True
				#win()
			elif s==8:
				tile.tile8=tile.turn
				return True
				#win()
			elif s==9:
				return True
				tile.tile9=tile.turn
				#win()
		else:
			return False
			#takeNaiveMove()
	except RecursionError:
		pass


def takeStrategicMove():
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	"""
	import tile
	if (validmove(1)==True and ((tile.tile2==tile.tile3==1) or (tile.tile4==tile.tile7==1) or (tile.tile5==tile.tile9==1) or (tile.tile2==tile.tile3==2) or (tile.tile4==tile.tile7==2) or (tile.tile5==tile.tile9==2))):
		tile.tile1=tile.turn
		return True

	if (validmove(2)==True and ((tile.tile1==tile.tile3==1) or (tile.tile5==tile.tile8==1) or (tile.tile1==tile.tile3==2) or (tile.tile5==tile.tile8==2))):
		tile.tile1=tile.turn
		return True

	if (validmove(3)==True and ((tile.tile1==tile.tile2==1) or (tile.tile5==tile.tile7==1) or (tile.tile6==tile.tile9==1) or (tile.tile1==tile.tile2==2) or (tile.tile5==tile.tile7==2) or (tile.tile6==tile.tile9==2))):
		tile.tile1=tile.turn
		return True

	if (validmove(4)==True and ((tile.tile1==tile.tile7==1) or (tile.tile5==tile.tile6==1) or (tile.tile1==tile.tile7==2) or (tile.tile5==tile.tile6==2))):
		tile.tile1=tile.turn
		return True

	if (validmove(5)==True and ((tile.tile1==tile.tile9==1) or (tile.tile3==tile.tile7==1) or (tile.tile2==tile.tile8==1) or (tile.tile4==tile.tile6==1) or (tile.tile1==tile.tile9==2) or (tile.tile3==tile.tile7==2) or (tile.tile2==tile.tile8==2) or (tile.tile4==tile.tile6==2))):
		tile.tile1=tile.turn
		return True

	if (validmove(6)==True and ((tile.tile3==tile.tile9==1) or (tile.tile4==tile.tile5==1) or (tile.tile3==tile.tile9==2) or (tile.tile4==tile.tile5==2))):
		tile.tile1=tile.turn
		return True

	if (validmove(7)==True and ((tile.tile3==tile.tile5==1) or (tile.tile8==tile.tile9==1) or (tile.tile1==tile.tile4==1) or (tile.tile3==tile.tile5==2) or (tile.tile8==tile.tile9==2) or (tile.tile1==tile.tile4==2))):
		tile.tile1=tile.turn
		return True

	if (validmove(8)==True and ((tile.tile7==tile.tile9==1) or (tile.tile2==tile.tile5==1) or (tile.tile7==tile.tile9==2) or (tile.tile2==tile.tile5==2))):
		tile.tile1=tile.turn
		return True

	if (validmove(9)==True and ((tile.tile1==tile.tile5==1) or (tile.tile7==tile.tile8==1) or (tile.tile3==tile.tile6==1) or (tile.tile1==tile.tile5==2) or (tile.tile7==tile.tile8==2) or (tile.tile3==tile.tile6==2))):
		tile.tile1=tile.turn
		return True


	if(validmove(5)==True):
		tile.tile5=tile.turn
		return True

	elif(validmove(7)==True):
		tile.tile7=tile.turn
		return True

	elif(validmove(3)==True):
		tile.tile3=tile.turn
		return True

	elif(validmove(1)==True):
		tile.tile1=tile.turn
		return True

	elif(validmove(9)==True):
		tile.tile9=tile.turn
		return True

	elif(validmove(2)==True):
		tile.tile2=tile.turn
		return True

	elif(validmove(4)==True):
		tile.tile4=tile.turn
		return True

	elif(validmove(6)==True):
		tile.tile6=tile.turn
		return True

	elif(validmove(8)==True):
		tile.tile8=tile.turn
		return True

	else:
		return False
		
def validBoard():
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""
	import tile	
	if (tile.move1==tile.move2) or (tile.move1==(tile.move2 +1)):
		return True
	else:
		return False

def game(gametype=1):
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	import tile
	if gametype==1:
		data()
		while ((win()==False) and ((tile.move1 + tile.move2)<9)):
			if validBoard() and (tile.turn==tile.player1):
				if takeNaiveMove():	
					tile.move1+=1
					tile.turn=tile.player2
			elif validBoard() and (tile.turn==tile.player2):
				if takeNaiveMove():
					tile.move2+=1
					tile.turn=tile.player1
			if (4<(tile.move1 + tile.move2)<10):
				if(win()):
					if ((tile.move1 + tile.move2)%2)==1:
						return 1
					else:
						return 2
					break
		if win()==False:
			return 0

	elif gametype==2:
		data()
		while ((win()==False) and ((tile.move1 + tile.move2)<9)):
			if validBoard() and (tile.turn==tile.player1):
				if takeNaiveMove():	
					tile.move1+=1
					tile.turn=tile.player2
			elif validBoard() and (tile.turn==tile.player2):
				if takeStrategicMove():
					tile.move2+=1
					tile.turn=tile.player1
			if (4<(tile.move1 + tile.move2)<10):
				if(win()):
					if ((tile.move1 + tile.move2)%2)==1:
						return 1
					else:
						return 2
					break
		if win()==False:
			return 0

	elif gametype==3:
		data()
		while ((win()==False) and ((tile.move1 + tile.move2)<9)):
			if validBoard() and (tile.turn==tile.player1):
				if takeStrategicMove():	
					tile.move1+=1
					tile.turn=tile.player2
			elif validBoard() and (tile.turn==tile.player2):
				if takeStrategicMove():
					tile.move2+=1
					tile.turn=tile.player1
			if (4<(tile.move1 + tile.move2)<10):
				if (win()==True):
					if ((tile.move1 + tile.move2)%2)==1:
						return 1
					else:
						return 2
					break
		if win()==False:
			return 0

def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	import tile
	tile.c=0
	for i in range(n):
		if game(1)==1:
			tile.c+=1
	prob1=(float(tile.c))/n
	return prob1	

def game2(n):
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	import tile
	tile.c=0
	for i in range(n):
		if game(2)==1:
			tile.c+=1
	prob1=(float(tile.c))/n
	return prob1

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	import tile
	tile.c=0
	for i in range(n):
		if game(3)==1:
			tile.c+=1
	prob1=(float(tile.c))/n
	return prob1