#KANISHK RANA
#2017241
#Assignment-2, Game Tic-tac-toe

#SOURCE OF STRATEGY 
#WHEN PLAYED AGAINST GOOGLE'S VERSION OF TIC TAC TOE considering the fact that for a program all the corners & the edges hold equal weightage . Hence playing in its impossible mode is quivalent of playing a game of intelligent vs intelligent and thus the cases are made in such a way that forces a draw
#Playing in an easy mode is equivalent to playing a game between an intelligent vs Naive and thus the first set of test cases are defined as such
#PLAYING GAMES WITH GOOGLE HELPED ME DESIGN MY STRATEGY FOR THIS GAME a picture to is hereby attached to show all the possible reactions of google's code to a particular move

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

import random 
# There are 2 players: player1 and player2
player1=1
player2=2


# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2



# turn variable defines whose turn is now


def resetboard():
		import tile
		tile.turn=1
		tile.tile1=0
		tile.tile2=0
		tile.tile3=0
		tile.tile4=0
		tile.tile5=0
		tile.tile6=0
		tile.tile7=0
		tile.tile8=0
		tile.tile9=0
	



def validmove(move):
	
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	import tile
	if move==0:
		return True
	else:
		return False
def win():
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a coloumn
		iii) in a diagonal
	"""
	import tile  
	#the important thing to note here is that we could have not assigned any value to tiles ie 1 or 2 but that would have created an 		  error in which the combination of 0 0 0 would have resulted in a win situtaion which is absolutely absurd

	if (tile.tile1==1 and tile.tile1==tile.tile2 and tile.tile2==tile.tile3 and tile.tile3==tile.tile1) or (tile.tile4==1 and tile.tile4==tile.tile5 and tile.tile5==tile.tile6 and tile.tile6==tile.tile4) or (tile.tile7==1 and tile.tile7==tile.tile8 and tile.tile8==tile.tile9 and tile.tile9==tile.tile7) or (tile.tile1==1 and tile.tile1==tile.tile4 and tile.tile4==tile.tile7 and tile.tile7==tile.tile1) or (tile.tile2==1 and tile.tile2==tile.tile5 and tile.tile5==tile.tile8 and tile.tile8==tile.tile2) or(tile.tile3==1 and tile.tile3==tile.tile6 and tile.tile6==tile.tile9 and tile.tile9==tile.tile3) or (tile.tile1==1 and tile.tile1==tile.tile5 and tile.tile5==tile.tile9 and tile.tile9==tile.tile1) or (tile.tile3==1 and tile.tile3==tile.tile5 and tile.tile5==tile.tile7 and tile.tile7==tile.tile3):
		tile.p1win+=1
				
		return True
		
	elif (tile.tile1==2 and tile.tile1==tile.tile2 and tile.tile2==tile.tile3 and tile.tile3==tile.tile1) or (tile.tile4==2 and tile.tile4==tile.tile5 and tile.tile5==tile.tile6 and tile.tile6==tile.tile4) or (tile.tile7==2 and tile.tile7==tile.tile8 and tile.tile8==tile.tile9 and tile.tile9==tile.tile7) or (tile.tile1==2 and tile.tile1==tile.tile4 and tile.tile4==tile.tile7 and tile.tile7==tile.tile1) or (tile.tile2==2 and tile.tile2==tile.tile5 and tile.tile5==tile.tile8 and tile.tile8==tile.tile2) or (tile.tile3==2 and tile.tile3==tile.tile6 and tile.tile6==tile.tile9 and tile.tile9==tile.tile3) or (tile.tile1==2 and tile.tile1==tile.tile5 and tile.tile5==tile.tile9 and tile.tile9==tile.tile1) or (tile.tile3==2 and tile.tile3==tile.tile5 and tile.tile5==tile.tile7 and tile.tile7==tile.tile3):
		tile.p2win+=1		#so much obviuosness for variable name !!!!
	
		return True
		
	else:
		return False	
	
def takeNaiveMove():
	
	
	import tile
	import random
	a=1
	
	while a<2:
		x=random.randint(1,9)
		
		if x==1 and validmove(tile.tile1):
			if tile.turn==tile.player1:
				tile.tile1=1
				tile.turn=tile.player2			
				a+=1
			else:
				tile.tile1=2
				tile.turn=tile.player1
				a=a+1
			

		elif x==2 and validmove(tile.tile2):
			if tile.turn==tile.player1:
				tile.tile2=1
				tile.turn=tile.player2			
				a=a+1
			else:
				tile.tile2=2
				tile.turn=tile.player1
				a=a+1
		
	
		elif x==3 and validmove(tile.tile3):
			if tile.turn==tile.player1:
				tile.tile3=1
				tile.turn=tile.player2			
				a=a+1
			else:
				tile.tile3=2
				tile.turn=tile.player1
				a=a+1
	
		elif x==4 and validmove(tile.tile4):
			if tile.turn==tile.player1:
				tile.tile4=1
				tile.turn=tile.player2			
				a=a+1
			else:
				tile.tile4=2
				tile.turn=tile.player1
				a=a+1
		
		elif x==5 and validmove(tile.tile5):
			if tile.turn==tile.player1:
				tile.tile5=1
				tile.turn=tile.player2			
				a=a+1
			else:
				tile.tile5=2
				tile.turn=tile.player1
				a=a+1
			

		elif x==6 and validmove(tile.tile6):
			if tile.turn==tile.player1:
				tile.tile6=1
				tile.turn=tile.player2			
				a=a+1
			else:
				tile.tile6=2
				tile.turn=tile.player1
				a=a+1
			

		elif x==7 and validmove(tile.tile7):
			if tile.turn==tile.player1:
				tile.tile7=1
				tile.turn=tile.player2			
				a=a+1
			else:
				tile.tile7=2
				tile.turn=tile.player1
				a=a+1
		
		elif x==8 and validmove(tile.tile8):
			if tile.turn==tile.player1:
				tile.tile8=1
				tile.turn=tile.player2			
				a=a+1
			else:
				tile.tile8=2
				tile.turn=tile.player1
				a=a+1
	
		elif x==9 and validmove(tile.tile9):
			if tile.turn==tile.player1:
				tile.tile9=1
				tile.turn=tile.player2			
				a=a+1
			else:
				tile.tile9=2
				tile.turn=tile.player1
				a=a+1
		return None
		
	

	

			
	
	
				

def takeStrategicMove():
	#as attached with this project are some images which show the countless combinations if two impossible players go head to head with eac other
	#the code should thus be avoided in which it just checks a force draw condition because in that case a naive player can also trigger a sequence due to which an intelligent player plays like forcing a draw even with a naive player
	#thus the strategy is strictly categorized in two categories and they are such that either it checks if it wins in the next move or it plays a move which contributes towards a forced draw
	
	#SOURCE OF STRATEGY 
#WHEN PLAYED AGAINST GOOGLE'S VERSION OF TIC TAC TOE considering the fact that for a program all the corners & the edges hold equal weightage . Hence playing in its impossible mode is quivalent of playing a game of intelligent vs intelligent and thus the cases are made in such a way that forces a draw
#Playing in an easy mode is equivalent to playing a game between an intelligent vs Naive and thus the first set of test cases are defined as such
#PLAYING GAMES WITH GOOGLE HELPED ME DESIGN MY STRATEGY FOR THIS GAME
	
	# First, check if we can win in the next move ie this part of code is basically triggered when a game between naive and intelligent palyer takes place because if that was not the case an intelligent player by defintion always face a scenario where he has to block a move to induce a forced draw
	


#checking a if row combination is possible you may find the too many combinations but they are backed by simple reasoning that given a row i could have chosen 2 tiles in 3c2 ways which equals 3 hence 3 combinations of each row
	import tile
	if(tile.tile1==tile.tile2==tile.turn and validmove(tile.tile3)==True):
		tile.tile3=tile.turn
		if tile.turn==2:
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif(tile.tile1==tile.tile3==tile.turn and validmove(tile.tile2)==True):
		tile.tile2=tile.turn
		if tile.turn==2:
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif (tile.tile2==tile.tile3==tile.turn and validmove(tile.tile1)==True):
		tile.tile1=tile.turn
		if tile.turn==2:
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif (tile.tile6==tile.tile5==tile.turn and validmove(tile.tile4)==True):
		tile.tile4=tile.turn
		if tile.turn==2:
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif (tile.tile6==tile.tile4==tile.turn and validmove(tile.tile5)==True):
		tile.tile5=tile.turn
		if tile.turn==2:
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif (tile.tile4==tile.tile5==tile.turn and validmove(tile.tile6)==True):
		tile.tile6=tile.turn
		if tile.turn==2:
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif(tile.tile9==tile.tile8==tile.turn and validmove(tile.tile7)==True):
		tile.tile7=tile.turn
		if tile.turn==2:
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif (tile.tile8==tile.tile7==tile.turn and validmove(tile.tile9)==True):
		tile.tile9=tile.turn
		if tile.turn==2:
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif (tile.tile9==tile.tile7==tile.turn and validmove(tile.tile8)==True):
		tile.tile8=tile.turn
		if tile.turn==2:
			tile.p2win+=1
		else:
			tile.p1win+=1
		


#checking the column combination 
	if(tile.tile1==tile.tile4==tile.turn and validmove(tile.tile7)==True):
		tile.tile7=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif (tile.tile1==tile.tile7==tile.turn and validmove(tile.tile4)==True):
  		tile.tile4=tile.turn
  		if tile.turn==2:
  			tile.p2win+=1
  		else:
  			tile.p1win+=1
		
	elif (tile.tile4==tile.tile7==tile.turn and validmove(tile.tile1)==True):
		tile.tile1=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
		 
	elif (tile.tile2==tile.tile5==tile.turn and validmove(tile.tile8)==True):
		tile.tile8=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
		
	elif (tile.tile2==tile.tile8==tile.turn and validmove(tile.tile5)==True):
		tile.tile5=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
		
	elif (tile.tile8==tile.tile5==tile.turn and validmove(tile.tile2)==True):
		tile.tile2=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif(tile.tile9==tile.tile6==tile.turn and validmove(tile.tile3)==True):
 		tile.tile3=tile.turn
 		if tile.turn==2:
 			tile.p2win+=1
 		else:
 			tile.p1win+=1
		 
	elif (tile.tile3==tile.tile6==tile.turn and validmove(tile.tile9)==True):
		tile.tile9=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
		 
	elif (tile.tile9==tile.tile3==tile.turn and validmove(tile.tile6)==True):
		tile.tile6=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
		

#checking diagonal combination
	if(tile.tile1==tile.tile5==tile.turn and validmove(tile.tile9)==True):
		tile.tile9=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1

	elif (tile.tile1==tile.tile9==tile.turn and validmove(tile.tile5)==True):
		tile.tile5=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
		
	elif (tile.tile5==tile.tile9==tile.turn and validmove(tile.tile1)==True):
		tile.tile1=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
		 
	elif (tile.tile3==tile.tile5==tile.turn and validmove(tile.tile7)==True):
		tile.tile7=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
		
	elif (tile.tile3==tile.tile7==tile.turn and validmove(tile.tile5)==True):
		tile.tile5=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
		
	elif (tile.tile7==tile.tile5==tile.turn and validmove(tile.tile3)==True):
		tile.tile3=tile.turn
		if tile.turn==2:		
			tile.p2win+=1
		else:
			tile.p1win+=1
	
	
#If a player is going to accidentally or strategically win block them before they do so while this may seem reduntant as the above code and the code below actually does the same thing!!! what the above code does is that if it finds a winning combination for itself it makes a move and the code below finds the winning move for the other one and makes a move and basically both parts does the same trick ie it makes a move on 2/3rd winning combination#
	
	if((tile.tile2==tile.tile3!=tile.turn and tile.tile2!=0 and validmove(tile.tile1)==True) or (tile.tile4==tile.tile7!=tile.turn and tile.tile4!=0 and validmove(tile.tile1)==True) or (tile.tile5==tile.tile9!=tile.turn and tile.tile5!=0 and validmove(tile.tile1)==True)):
		tile.tile1=tile.turn			#assign the turn to the tile ie 1 or 2 and change accordingly
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2		

	if((tile.tile1==tile.tile3!=tile.turn and tile.tile1!=0 and validmove(tile.tile2)==True) or (tile.tile5==tile.tile8!=tile.turn and tile.tile5!=0 and validmove(tile.tile2)==True)):
		tile.tile2=tile.turn			#assign the turn to the tile ie 1 or 2 and change accordingly
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	if((tile.tile1==tile.tile2!=tile.turn and tile.tile1!=0 and validmove(tile.tile3)==True) or (tile.tile6==tile.tile9!=tile.turn and tile.tile6!=0 and validmove(tile.tile3)==True) or (tile.tile5==tile.tile7!=tile.turn and tile.tile5!=0 and validmove(tile.tile3)==True)):
		tile.tile3=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	if((tile.tile1==tile.tile7!=tile.turn and tile.tile1!=0 and validmove(tile.tile4)==True) or (tile.tile5==tile.tile6!=tile.turn and tile.tile5!=0 and validmove(tile.tile4)==True)):	
		tile.tile4=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	if((tile.tile2==tile.tile8!=tile.turn and tile.tile2!=0 and validmove(tile.tile5)==True) or (tile.tile4==tile.tile6!=tile.turn and tile.tile4!=0 and validmove(tile.tile5)==True) or (tile.tile1==tile.tile9!=tile.turn and tile.tile1!=0 and validmove(tile.tile5)==True) or (tile.tile3==tile.tile7!=tile.turn and tile.tile3!=0 and validmove(tile.tile5)==True)):	
		tile.tile5=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	if((tile.tile3==tile.tile9!=tile.turn and tile.tile3!=0 and validmove(tile.tile6)==True) or (tile.tile4==tile.tile5!=tile.turn and tile.tile4!=0 and validmove(tile.tile6)==True)):	
		tile.tile6=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	if((tile.tile8==tile.tile9!=tile.turn and tile.tile8!=0 and validmove(tile.tile7)==True) or (tile.tile1==tile.tile4!=tile.turn and tile.tile1!=0 and validmove(tile.tile7)==True) or (tile.tile3==tile.tile5!=tile.turn and tile.tile3!=0 and validmove(tile.tile7)==True)):	
		tile.tile7=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	if((tile.tile2==tile.tile5!=tile.turn and tile.tile2!=0 and validmove(tile.tile8)==True) or (tile.tile7==tile.tile9!=tile.turn and tile.tile7!=0 and validmove(tile.tile8)==True)):	
		tile.tile8=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2


	if((tile.tile7==tile.tile8!=tile.turn and tile.tile7!=0 and validmove(tile.tile9)==True) or (tile.tile3==tile.tile6!=tile.turn and tile.tile3!=0 and validmove(tile.tile9)==True) or (tile.tile1==tile.tile5!=tile.turn and tile.tile1!=0 and validmove(tile.tile9)==True)):	
		tile.tile9=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2
	#default moves if none of the above triggers
	

	

	if(validmove(tile.tile3)==True):
		tile.turn3=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	if(validmove(tile.tile1)==True):
		tile.turn1=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	if(validmove(tile.tile9)==True):
		tile.turn9=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	
	if(validmove(tile.tile7)==True):
		tile.turn7=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2


	if(validmove(tile.tile4)==True):
		tile.turn4=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2
	if(validmove(tile.tile6)==True):
		tile.turn6=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2

	if(validmove(tile.tile8)==True):
		tile.turn8=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2	

	
	if(validmove(tile.tile2)==True):
		tile.turn2=tile.turn
		if tile.turn==2:
			tile.turn=1
		else:
			tile.turn=2
		

def validboard():
	import tile
	a=0
	b=0
	if(tile.tile1==1):
		a+=1
	if(tile.tile1==2):
		b+=1	
	if(tile.tile2==1):
		a+=1
	if(tile.tile2==2):
		b+=1	
	if(tile.tile3==1):
		a+=1
	if(tile.tile3==2):
		b+=1	
	if(tile.tile4==1):
		a+=1
	if(tile.tile4==2):
		b+=1	
	if(tile.tile5==1):
		a+=1
	if(tile.tile5==2):
		b+=1
	if(tile.tile6==1):
		a+=1
	if(tile.tile6==2):
		b+=1
	if(tile.tile7==1):
		a+=1
	if(tile.tile7==2):
		b+=1	
	if(tile.tile8==1):
		a+=1
	if(tile.tile8==2):
		b+=1	
	if(tile.tile9==1):
		a+=1
	if(tile.tile9==2):
		b+=1

	if(a>=b):
		return True
	else:
		return False	
	


	
def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	
	import tile
	tile.p1win=0
	tile.p2win=0
	for i in range(n):
		resetboard()
		for j in range(9):
			if tile.turn==1:
				takeNaiveMove()
				tile.turn=2
				
				if win():
					break
			else:
				takeNaiveMove()
				tile.turn=1
				
				if win():
					break
	
			
	prob1=float(tile.p1win)/int(n)
	
	print (prob1)
	return prob1


def game2(n):
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	
	import tile
	tile.p1win=0
	tile.p2win=0
	for i in range(n):
		resetboard()
		for j in range(9):
			
			if tile.turn==1:
								
				takeNaiveMove()
				tile.turn=2
				
				if win():
					break
			else:
				takeStrategicMove()
				tile.turn=1
				
				if win():
					break
	
			
	prob1=float(tile.p1win)/int(n)
	
	print(prob1)
	
	return prob1

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	
	import tile
	tile.p1win=0
	tile.p2win=0
	for i in range(n):
		resetboard()
		for j in range(9):
			if tile.turn==1:
				takeStrategicMove()
				tile.turn=2
				
				if win():
					break
			else:
				takeStrategicMove()
				tile.turn=1
				
				if win():
					break
	
			
	prob1=float(tile.p1win)/int(n)
	
	print(prob1)

	return prob1



	
