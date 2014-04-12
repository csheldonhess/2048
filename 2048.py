import random

def addanumber(board):
	
	while True:
		# we'll place the new number in a random x-y location on the board
		coordx = random.randint(0,3)
		coordy = random.randint(0,3)
		#print('y: ' + str(coordy) + ' x: ' + str(coordx))		

		# 90% chance of the new number being a 2; 10% chance of a 4
		pickanumber = random.randint(0,9)
		if pickanumber < 1:
			newboardnumber = 4
		else:
			newboardnumber = 2

		if board[coordy][coordx] == 0:
			board[coordy][coordx] = newboardnumber
			break
		


def printboard(board, score):
	print('\n                                   Your score: ' + str(score))
	for y in range(0,4):
		tempstring = ' '
		for x in range(0,4):
			if board[y][x] == 0:
				toprint = '    '
			else:
				toprint = str(board[y][x])
				if board[y][x] < 1000:
					toprint = ' ' + toprint
				if board[y][x] < 100:
					toprint = toprint + ' '
				if board[y][x] < 10:
					toprint = ' ' + toprint
			if x == 3:
				tempstring = tempstring + toprint
			else:
				tempstring = tempstring + toprint + ' | '
		print(tempstring)
		if y < 3:
			print(' --------------------------')
	print()


# initialize the board - this is ugly, but effective
theboard = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
playerscore = 0

# put the first two values on the board
addanumber(theboard)
addanumber(theboard)
printboard(theboard, playerscore)
maxnum = 0

while maxnum < 2048:
	
	command = input('Choose [U]p, [D]own, [L]eft, [R]ight, or [Q]uit, and hit "Enter": ')
	if len(command) >= 1:
		if command[0] == 'q' or command[0] == 'Q':
			break
		elif command[0] == 'u' or command[0] == 'U':
			print('You picked up')
			for x in range(0, 4): 
				for y in range(0, 4): # look for topmost nonzero element
					if theboard[y][x] != 0 and y < 3: # if y == 3, no need to look further
						for yprime in range(y + 1, 4): 
							if theboard[yprime][x] != 0: # so there IS a number there
								if theboard[yprime][x] == theboard[y][x]:
									theboard[y][x] = 2 * theboard[y][x]
									if theboard[y][x] > maxnum: # looking for win condition
										maxnum = theboard[y][x]
									playerscore = playerscore + theboard[y][x] # keepin' score
									theboard[yprime][x] = 0
									break # out of yprime loop to prevent double matches
								else: # there's a number, not zero, but it doesn't match
									break # non-matching number, not interesting, leave yprime loop
							# implied else: theboard[yprime][x] WAS zero, so look further
				for y in range(0, 4):
					if theboard[y][x] == 0 and y < 3: # empty spot! and somewhere to shift!
						for yprime in range(y + 1, 4):
							if theboard[yprime][x] != 0:
								theboard[y][x] = theboard[yprime][x]
								theboard[yprime][x] = 0
								break # gets us out of yprime loop, to prevent overwriting
			addanumber(theboard)
			printboard(theboard, playerscore)	
		elif command[0] == 'r' or command[0] == 'R':
			print('You picked right')
			for y in range(0, 4): # 0 through 3
				for x in range(3, -1, -1): # 3, 2, 1, 0 - weird-looking, but right
					# we are looking for the LAST nonzero element (in this case, rightmost)
					if theboard[y][x] != 0 and x > 0: # if x == 0, we need not look more left
						for xprime in range(x-1, -1, -1):
							if theboard[y][xprime] != 0: # found a number to the left!
								if theboard[y][xprime] == theboard[y][x]:
									theboard[y][x] = 2 * theboard[y][x]
									playerscore = playerscore + theboard[y][x]
									if theboard[y][x] > maxnum:
										maxnum = theboard[y][x]
									theboard[y][xprime] = 0
									break # prevents double-matches
								else:
									break # out of xprime loop - non-matching #'s can't combine
							# implied else: theboard[y][xprime] was zero, so keep looking
				for x in range(3, -1, -1):
					if theboard[y][x] == 0 and x > 0:
						for xprime in range(x-1, -1, -1):
							if theboard[y][xprime] != 0: 
								theboard[y][x] = theboard[y][xprime]
								theboard[y][xprime] = 0
								break # gets us out of xprime loop; important so we don't overwrite
			addanumber(theboard)
			printboard(theboard, playerscore)	
		elif command[0] == 'd' or command[0] == 'D':
			print('You picked down')
			for x in range(0, 4): 
				for y in range(3, -1, -1): # looking for bottommost nonzero element
					if theboard[y][x] != 0 and y > 0: # if y == 0, we're at the top
						for yprime in range(y-1, -1, -1):
							if theboard[yprime][x] != 0: # we have a number! is it a match?
								if theboard[yprime][x] == theboard[y][x]:
									theboard[y][x] = theboard[y][x] * 2
									if theboard[y][x] > maxnum:
										maxnum = theboard[y][x]
									playerscore = playerscore + theboard[y][x]
									theboard[yprime][x] = 0
									break # out of yprime loop to prevent double-matches
								else: # it was a number, but didn't match, boooooo
									break # gets us out of yprime
							# implied else: theboard[yprime][x] was 0; look at next y'
				for y in range(3, -1, -1):
					if theboard[y][x] == 0 and y > 0: # a space we can shift into!
						for yprime in range(y-1, -1, -1):
							if theboard[yprime][x] != 0:
								theboard[y][x] = theboard[yprime][x]
								theboard[yprime][x] = 0
								break # leaving the yprime loop to avoid overwriting!
			addanumber(theboard)
			printboard(theboard, playerscore)	
		elif command[0] == 'l' or command[0] == 'L':
			print('You picked left')
			for y in range(0, 4):
				for x in range(0, 4): # we want the last (leftmost) nonzero element
					if theboard[y][x] != 0 and x < 3: # no need to go further if we're @ end
						for xprime in range(x+1, 4):
							if theboard[y][xprime] != 0: # found a number to the right!
								if theboard[y][x] == theboard[y][xprime]:
									theboard[y][x] = 2 * theboard[y][x]
									playerscore = playerscore + theboard[y][x]
									if theboard[y][x] > maxnum:
										maxnum = theboard[y][x]
									theboard[y][xprime] = 0
									break # out of xprime loop, to prevent double-matches
								else:
									break # out of xprime loop, because we don't have a match
							# implied else: theboard[y][xprime] was zero, so keep looking
				for x in range(0, 4): # now we shift everything to the left
					if theboard[y][x] == 0 and x < 3:
						for xprime in range(x+1, 4):
							if theboard[y][xprime] != 0:
								theboard[y][x] = theboard[y][xprime]
								theboard[y][xprime] = 0
								break # got to leave the xprime loop so we don't overwrite
			addanumber(theboard)
			printboard(theboard, playerscore)
		else: 
			print('That wasn\'t one of the choices. Try again?')
	else: # no input
		print('You need to enter a character.')

	# if there are no empty squares left, the game is over
	zeroes = 0
	# UNLESS there are valid moves left!
	playsleft = False
	
	for y in range(0, 4):
		zeroes = zeroes + theboard[y].count(0)
		if zeroes > 0: # why do this more times than needed, right?
			break
		for x in range(0,4):
			if x < 3 and theboard[y][x+1] == theboard[y][x]:
				playsleft = True
				break
			if y < 3 and theboard[y+1][x] == theboard[y][x]:
				playsleft = True
				break
		if playsleft == True:
			break
	
	if zeroes == 0 and playsleft == False:
		print('\nGame Over')
		break

if maxnum == 2048:
	print('\nWow! Many squares! Such win!\n')
else:
	print('\nSee you next time!\n')







