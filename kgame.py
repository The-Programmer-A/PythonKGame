#
# NWEN 241 Programming Assignment 5
# kgame.py Python Source File
#
# Name:
# Student ID:
# 
# IMPORTANT: Implement the functions specified in kgame.h here. 
# You are free to implement additional functions that are not specified in kgame.h here.
#

import random

# This is the title of the game 
KGAME_TITLE = "The K-Game (Python Edition)"

# This is the file name of the saved game state 
KGAME_SAVE_FILE = "kgame.sav"

# Number of tiles per side 
KGAME_SIDES = 4

# Output buffer size in bytess 
KGAME_OUTPUT_BUFLEN = ((18*40)+1)

# Arrow keys 
dirs = { 'UP': 1, 'DOWN': 2, 'LEFT': 3, 'RIGHT': 4 }

# Keys accepted by game 
inputs = { 'LOAD': 5, 'SAVE': 6, 'EXIT': 7} 

#game is a dictionary first key is score which has value of ints
# second key is board which acts as a 2D array
def kgame_init(game):
    game['score'] = 0 # intialize the score
    game['board'] = [[' ' for x in range(KGAME_SIDES)] for y in range(KGAME_SIDES)] # board is a 4 x 4 array


def kgame_add_random_tile(game):
    # find random, but empty tile
    # FIXME: will go to infinite loop if no empty tile
    
	count = 0;
	
	for rows in range(4):
		for cols in range(4):
			if game['board'][rows][cols] != ' ': # if cells in the board are occupied
				count += 1;
			
		
	if count == 16: # if there is no free cells then exit (stop infinate loop)
		return
	

	while True:
		row = random.randint(0, KGAME_SIDES-1)
		col = random.randint(0, KGAME_SIDES-1)
		if game['board'][row][col] == ' ':
			break
	
	# place to the random position 'A' or 'B' tile
	game['board'][row][col] = 'A' 
	if random.randint(0, 2) == 1:
		game['board'][row][col] = 'B'
		
		


def kgame_render(game):
    # FIXME: Implement correctly (task 1)
	'''
	 because python has no type declearation we must be careful of what we asign 
	 a varibale. A varibale should always be of the same type otherwise some
	 actions on the varible might spit a problem at you
	'''
	output_buffer = str(game['score']) # display the score
	output_buffer += ' \n'
	
	kgame_add_random_tile(game)
	
	# creating the top
	output_buffer += "+---"  * 4 
	#output_buffer += "+" 
	output_buffer += "+\n"
	
	# creating the middle
	for rows in range(4):
		for cols in range(4):
			ktile = game['board'][rows][cols]
			
			output_buffer += "|  " 
			output_buffer += ktile
			
		output_buffer += "|"
		output_buffer += "\n"	
		# creating the bottom
		output_buffer += "+---" * 4
		#output_buffer += "+" 
		output_buffer += '+\n'
	  
	
	return output_buffer

def kgame_is_won(game):
    # FIXME: Implement correctly (task 2)
    # if there a K on the board then the game is won
    
	for rows in range(4):
		for cols in range(4):
			if game['board'] [rows][cols] == 'K':
				return True
	
	
	return False

def kgame_is_move_possible(game): 
    # FIXME: Implement correctly (task 3)
    # return True;
    
    #if there is at least one space on the board

	for rows in range(4):
		for cols in range(4):
			if game['board'] [rows][cols] == ' ':
				return True
	
	#if there are 2 adjacent cells of same value horizontal
	
	for rows in range(0, 3):
		for cols in range(0, 3):
			if game['board'][rows][cols] == game['board'][rows][cols+1]: #adjacent horizontal
				return True
	
	#if there are 2 adjacent cells of same value vetical
	for cols in range(3,-1,-1):
		for rows in range(3,0,-1):
			if game['board'][rows][cols] == game['board'][rows-1][cols]:
				return True
	
	# The board had no spaces, no adjacent cells Verticall and Horizonataly of same letter
	return False


def kgame_update(game, direction):
    # FIXME: Implement correctly (task 4)
    # return True;    
	moved = 0
	if direction == 1: # the direction was up
		#implementing the shifter
		
		for cols in range(3,-1,-1): # starting at the bottom right going through all cols
			shifter = 0
			while(shifter <= 4):
				for rows in range(3, 0, -1):  # starting at the last row going till row 1 NOT 0
					if game['board'][rows-1][cols] == ' ':
						game['board'][rows-1][cols] = game['board'][rows][cols]
						game['board'][rows][cols] = ' '	
					
				shifter += 1
				moved = 1
			
			#allowing to merge
			shifter1 = 0
			while (shifter1 < 1):
				for mergeRows in range(3, 0, -1):
					if ((game['board'][mergeRows][cols] == game['board'][mergeRows-1][cols]) & (game['board'][mergeRows][cols] != ' ')):
						game['board'][mergeRows-1][cols] = chr(ord(game['board'][mergeRows-1][cols]) + 1 ) 
						game['board'][mergeRows][cols] = ' '
						game['score'] += updateScore(ord(game['board'][mergeRows-1][cols]))
						break
					
				shifter1 += 1
				moved = 1
			
			#shift everything as far up as possible
			shifter2 = 0
			while(shifter2 < 1):
				for rows in range(3, 0, -1):
					if game['board'][rows-1][cols] == ' ':
						game['board'][rows-1][cols] = game['board'][rows][cols]
						game['board'][rows][cols] = ' '
					
				shifter2 += 1
				moved = 1
			
	
	if direction == 2: # the direction was down
		# implementing the shifter
		
		for cols in range(4):
			shifter = 0
			while( shifter <= 4):
				for rows in range(3):
					if game['board'][rows+1][cols] == ' ':
						game['board'][rows+1][cols] = game['board'][rows][cols]
						game['board'][rows][cols] = ' '
					
				shifter += 1
				moved = 1
			
			#allowing to merge
			shifter1 = 0
			while(shifter1 < 1):
				for mergeRows in range(3):
					if ((game['board'][mergeRows][cols] == game['board'][mergeRows+1][cols]) & (game['board'][mergeRows][cols] != ' ')):
						game['board'][mergeRows+1][cols] = chr(ord(game['board'][mergeRows+1][cols]) + 1)
						game['board'][mergeRows][cols] = ' '
						game['score'] += updateScore(ord(game['board'][mergeRows+1][cols]))
						break
					
				shifter1 += 1
				moved = 1
			
			#shift as far down
			shifter2 = 0
			while (shifter2 <= 4):
				for rows in range(3):
					if game['board'][rows+1][cols] == ' ':
						game['board'][rows+1][cols] = game['board'][rows][cols]
						game['board'][rows][cols] = ' '
					
					
				shifter2 += 1
				moved = 1
			
		
		#return True
		
	if direction == 3: # the direction was left LEFT WROKS
		for rows in range(4): # go through all the rows
			shifter = 0
			while(shifter <= 4):
				for cols in range(1, 4): # start on the second row so can check left
					if game['board'][rows][cols-1] == ' ':
						game['board'][rows][cols-1] = game['board'][rows][cols]
						game['board'][rows][cols] = ' '
					
				shifter += 1
				moved = 1
			
			
			shifter1 = 0 
			while (shifter1 < 1):
				for mergeCols in range(1, 4):
					if ((game['board'][rows][mergeCols] == game['board'][rows][mergeCols-1]) & (game['board'][rows][mergeCols] != ' ')):
						game['board'][rows][mergeCols-1] = chr(ord(game['board'][rows][mergeCols-1]) + 1)
						game['board'][rows][mergeCols] = ' '
						game['score'] += updateScore(ord(game['board'][rows][mergeCols-1]))
						break;
					
				shifter1 += 1
				moved = 1
			
			shifter2 = 0
			while(shifter2 <= 4):
				for cols in range(1, 4): # start on the second row so can check left
					if game['board'][rows][cols-1] == ' ':
						game['board'][rows][cols-1] = game['board'][rows][cols]
						game['board'][rows][cols] = ' '
					
				shifter2 += 1
				moved = 1
			
		
		#return True
		
	if direction == 4: # the direction was right
		for rows in range(3, -1, -1):
			shifter = 0
			while (shifter <= 4):
				for cols in range(2, -1, -1):
					if game['board'][rows][cols+1] == ' ':
						game['board'][rows][cols+1] = game['board'][rows][cols]
						game['board'][rows][cols] = ' '
					
				shifter += 1
				moved = 1
			
			# allowing to merge
			shifter1 = 0
			while(shifter1 < 1):
				for mergeCols in range(2, -1, -1):
					if ((game['board'][rows][mergeCols] == game['board'][rows][mergeCols+1]) & (game['board'][rows][mergeCols] != ' ')):
						game['board'][rows][mergeCols+1] = chr(ord(game['board'][rows][mergeCols+1]) + 1)
						game['board'][rows][mergeCols] = ' '
						game['score'] += updateScore(ord(game['board'][rows][mergeCols+1]))
						break
					
				shifter1 += 1
				moved = 1
			
			# shift all the way right
			shifter2 = 0
			while(shifter2 <= 4):
				for cols in range(2, -1, -1):
					if game['board'][rows][cols+1] == ' ':
						game['board'][rows][cols+1] = game['board'][rows][cols]
						game['board'][rows][cols] = ' '
					
				shifter2 += 1
				moved = 1
	
	if moved == 1:
		return True
	
	
	return False	
	
def updateScore(letter):
	return (1**(letter - 65)*2)
	
		
def kgame_save(game):
    # FIXME: Implement correctly (task 5)
	fw = open(KGAME_SAVE_FILE, "w")
	
	if(fw is None): #valid inputs
		return False

	
	for i in range(4):
		for j in range(4):
			if game['board'][i][j] == ' ':
				fw.write("-")
			else:
				fw.write(game['board'][i][j])
			
		
	fw.write(str(game['score']))
	fw.close()


def kgame_load(game):
    # FIXME: Implement correctly (task 6)
	fr = open(KGAME_SAVE_FILE, "r")
	
	validInputs = (1, 2, 3, )
	
	if fr is None: # valid inputs
		return
	for i in range(4):
		for j in range(4):
			c = fr.read(1)
			if c == "-":
				game['board'][i][j] = ' '
			else:
				game['board'][i][j] = c
			
		
	
	game['score'] = int (fr.read())
	fr.close()
	return True

