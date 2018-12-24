import random 


player1=1
player2=2

p1count = 0
p2count = 0




tile1= 0    
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0

turn = player1

def validmove(move):
	
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn,player1,player2


	if(tile1==0 and move ==1):
		return True
	elif(tile2==0 and move ==2):
		return True
	elif(tile3==0 and move ==3):
		return True
	elif(tile4==0 and move ==4):
		return True
	elif(tile5==0 and move ==5):
		return True
	elif(tile6==0 and move ==6):
		return True
	elif(tile7==0 and move ==7):
		return True
	elif(tile8==0 and move ==8):
		return True
	elif(tile9==0 and move ==9):
		return True
	else:
		return False


def win():
	
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn,player1,player2

	if(tile1==1 and tile2==1 and tile3==1):
		return True
	elif(tile4==1 and tile5==1 and tile6==1):
		return True
	elif(tile7==1 and tile8==1 and tile9==1):
		return True
	elif(tile1==1 and tile4==1 and tile7==1):
		return True
	elif(tile2==1 and tile5==1 and tile8==1):
		return True
	elif(tile3==1 and tile6==1 and tile9==1):
		return True
	elif(tile1==1 and tile5==1 and tile9==1):
		return True
	elif(tile3==1 and tile5==1 and tile7==1):
		return True
	elif(tile1==2 and tile2==2 and tile3==2):
		return True
	elif(tile4==2 and tile5==2 and tile6==2):
		return True
	elif(tile7==2 and tile8==2 and tile9==2):
		return True
	elif(tile1==2 and tile4==2 and tile7==2):
		return True
	elif(tile2==2 and tile5==2 and tile8==2):
		return True
	elif(tile3==2 and tile6==2 and tile9==2):
		return True
	elif(tile1==2 and tile5==2 and tile9==2):
		return True
	elif(tile3==2 and tile5==2 and tile7==2):
		return True
	
	
def turnchange():
	global turn,player1,player2
	if(turn==player1):
		turn=player2
	else:
		turn=player1



def takeNaiveMove():
	
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn,player1,player2
	while(True):
		rantile = random.randint(1,9)
		if validmove(rantile):
			return rantile
		

	
			
def takeStrategicMove():
	
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn,player1,player2
	ptile = turn
	ntile = turnchange()
	if(tile1==tile2==ptile and validmove(3)):	
		tile3 = ntile
		return 3
	elif(tile4==tile5==ptile and validmove(6)):	
		tile6 = ntile
		return 6
	elif(tile7==tile8==ptile and validmove(9)):	
		tile9 = ntile
		return 9
	elif(tile2==tile3==ptile and validmove(1)):
		tile1 = ntile
		return 1
	elif(tile5==tile6==ptile and validmove(4)):	
		tile4 = ntile
		return 4
	elif(tile8==tile9==ptile and validmove(7)):	
		tile7 = ntile
		return 7
	elif(tile1==tile3==ptile and validmove(2)):	
		tile2 = ntile
		return 2
	elif(tile4==tile6==ptile and validmove(5)):	
		tile5 = ntile
		return 5
	elif(tile7==tile9==ptile and validmove(8)):	
		tile8 = ntile
		return 8
	elif(tile1==tile4==ptile and validmove(7)):	
		tile7 = ntile
		return 7
	elif(tile2==tile5==ptile and validmove(8)):	
		tile8 = ntile
		return 8
	elif(tile3==tile6==ptile and validmove(9)):	
		tile9 = ntile
		return 9
	elif(tile4==tile7==ptile and validmove(1)):	
		tile9 = ntile
		return 1
	elif(tile5==tile8==ptile and validmove(2)):	
		tile2 = ntile
		return 2
	elif(tile6==tile9==ptile and validmove(3)):	
		tile3 = ntile
		return 3
	elif(tile1==tile7==ptile and validmove(4)):	
		tile4 = ntile
		return 4
	elif(tile2==tile8==ptile and validmove(5)):	
		tile5 = ntile
		return 5
	elif(tile3==tile9==ptile and validmove(6)):	
		tile6 = ntile
		return 6
	elif(tile1==tile5==ptile and validmove(9)):	
		tile9 = ntile
		return 9
	elif(tile3==tile5==ptile and validmove(7)):	
		tile7 = ntile
		return 7
	elif(tile5==tile9==ptile and validmove(1)):	
		tile1 = ntile
		return 1
	elif(tile5==tile7==ptile and validmove(3)):	
		tile3 = ntile
		return 3
	elif(tile1==tile9==ptile and validmove(5)):	
		tile5 = ntile
		return 5
	elif(tile3==tile7==ptile and validmove(5)):	
		tile5 = ntile
		return 5





	elif(tile1==tile2==ntile and validmove(3)):	
		tile3 = ptile
		return 3
	elif(tile4==tile5==ntile and validmove(6)):	
		tile6 = ptile
		return 6
	elif(tile7==tile8==ntile and validmove(9)):	
		tile9 = ptile
		return 9
	elif(tile2==tile3==ntile and validmove(1)):
		tile1 = ptile
		return 1
	elif(tile5==tile6==ntile and validmove(4)):	
		tile4 = ptile
		return 4
	elif(tile8==tile9==ntile and validmove(7)):	
		tile7 = ptile
		return 7
	elif(tile1==tile3==ntile and validmove(2)):	
		tile2 = ptile
		return 2
	elif(tile4==tile6==ntile and validmove(5)):	
		tile5 = ptile
		return 5
	elif(tile7==tile9==ntile and validmove(8)):	
		tile8 = ptile
		return 8
	elif(tile1==tile4==ntile and validmove(7)):	
		tile7 = ptile
		return 7
	elif(tile2==tile5==ntile and validmove(8)):	
		tile8 = ptile
		return 8
	elif(tile3==tile6==ntile and validmove(9)):	
		tile9 = ptile
		return 9
	elif(tile4==tile7==ntile and validmove(1)):	
		tile9 = ptile
		return 1
	elif(tile5==tile8==ntile and validmove(2)):	
		tile2 = ptile
		return 2
	elif(tile6==tile9==ntile and validmove(3)):	
		tile3 = ptile
		return 3
	elif(tile1==tile7==ntile and validmove(4)):	
		tile4 = ptile
		return 4
	elif(tile2==tile8==ntile and validmove(5)):	
		tile5 = ptile
		return 5
	elif(tile3==tile9==ntile and validmove(6)):	
		tile6 = ptile
		return 6
	elif(tile1==tile5==ntile and validmove(9)):	
		tile9 = ptile
		return 9
	elif(tile3==tile5==ntile and validmove(7)):	
		tile7 = ptile
		return 7
	elif(tile5==tile9==ntile and validmove(1)):	
		tile1 = ptile
		return 1
	elif(tile5==tile7==ntile and validmove(3)):	
		tile3 = ptile
		return 3
	elif(tile1==tile9==ntile and validmove(5)):	
		tile5 = ptile
		return 5
	elif(tile3==tile7==ntile and validmove(5)):	
		tile5 = ptile
		return 5
	
	if(validmove(5)):
		tile5 = ptile
		return 5
	elif(validmove(1)):
		tile1 = ptile
		return 1
	elif(validmove(3)):
		tile3 = ptile
		return 3
	elif(validmove(7)):
		tile7 = ptile
		return 7
	elif(validmove(9)):
		tile9 = ptile
		return 9
	elif(validmove(2)):
		tile2 = ptile
		return 2
	elif(validmove(4)):
		tile4 = ptile
		return 4
	elif(validmove(6)):
		tile6 = ptile
		return 6
	elif(validmove(8)):
		tile8 = ptile
		return 8




def validBoard():
	
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn,player1,player2
	dif = p1count-p2count
	if abs(dif == 0 or dif == 1):
		return True
	else:
		return False

def game(gametype):
	
	
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn,player1,player2

	if(gametype==1):
		turn = player1
		for x in range(9):
			tile = takeNaiveMove()
			
			if tile == 1:
				tile1 = turn
			elif tile == 2:
				tile2 = turn
			elif tile == 3:
				tile3 = turn
			elif tile == 4:
				tile4 = turn
			elif tile == 5:
				tile5 = turn
			elif tile == 6:
				tile6 = turn
			elif tile == 7:
				tile7 = turn
			elif tile == 8:
				tile8 = turn
			elif tile == 9:
				tile9 = turn
			
			
			
			if((tile1==1 and tile2==1 and tile3==1) or (tile4==1 and tile5==1 and tile6==1) or(tile7==1 and tile8==1 and tile9==1) or (tile1==1 and tile4==1 and tile7==1) or (tile2==1 and tile5==1 and tile8==1) or (tile3==1 and tile6==1 and tile9==1) or (tile1==1 and tile5==1 and tile9==1) or (tile3==1 and tile5==1 and tile7==1)):
				return 1
			elif((tile1==2 and tile2==2 and tile3==2) or (tile4==2 and tile5==2 and tile6==2) or(tile7==2 and tile8==2 and tile9==2) or (tile1==2 and tile4==2 and tile7==2) or (tile2==2 and tile5==2 and tile8==2) or (tile3==2 and tile6==2 and tile9==2) or (tile1==2 and tile5==2 and tile9==2) or (tile3==2 and tile5==2 and tile7==2)):
				return 2
			
			turnchange()
		else:
			return 0

	if(gametype==2):
		turn = player1
		for x in range(9):
			if x%2==1:	
				tile = takeNaiveMove()
			elif x%2==0:
				tile = takeStrategicMove()
			
			if tile == 1:
				tile1 = turn
			elif tile == 2:
				tile2 = turn
			elif tile == 3:
				tile3 = turn
			elif tile == 4:
				tile4 = turn
			elif tile == 5:
				tile5 = turn
			elif tile == 6:
				tile6 = turn
			elif tile == 7:
				tile7 = turn
			elif tile == 8:
				tile8 = turn
			elif tile == 9:
				tile9 = turn
			
			
			
			if((tile1==1 and tile2==1 and tile3==1) or (tile4==1 and tile5==1 and tile6==1) or(tile7==1 and tile8==1 and tile9==1) or (tile1==1 and tile4==1 and tile7==1) or (tile2==1 and tile5==1 and tile8==1) or (tile3==1 and tile6==1 and tile9==1) or (tile1==1 and tile5==1 and tile9==1) or (tile3==1 and tile5==1 and tile7==1)):
				return 1
			elif((tile1==2 and tile2==2 and tile3==2) or (tile4==2 and tile5==2 and tile6==2) or(tile7==2 and tile8==2 and tile9==2) or (tile1==2 and tile4==2 and tile7==2) or (tile2==2 and tile5==2 and tile8==2) or (tile3==2 and tile6==2 and tile9==2) or (tile1==2 and tile5==2 and tile9==2) or (tile3==2 and tile5==2 and tile7==2)):
				return 2
			
			turnchange()
		else:
			return 0
	
	if(gametype==3):
		turn = player1
		for x in range(9):
			tile = takeStrategicMove()
			
			if tile == 1:
				tile1 = turn
			elif tile == 2:
				tile2 = turn
			elif tile == 3:
				tile3 = turn
			elif tile == 4:
				tile4 = turn
			elif tile == 5:
				tile5 = turn
			elif tile == 6:
				tile6 = turn
			elif tile == 7:
				tile7 = turn
			elif tile == 8:
				tile8 = turn
			elif tile == 9:
				tile9 = turn
			
			
			
			if((tile1==1 and tile2==1 and tile3==1) or (tile4==1 and tile5==1 and tile6==1) or(tile7==1 and tile8==1 and tile9==1) or (tile1==1 and tile4==1 and tile7==1) or (tile2==1 and tile5==1 and tile8==1) or (tile3==1 and tile6==1 and tile9==1) or (tile1==1 and tile5==1 and tile9==1) or (tile3==1 and tile5==1 and tile7==1)):
				return 1
			elif((tile1==2 and tile2==2 and tile3==2) or (tile4==2 and tile5==2 and tile6==2) or(tile7==2 and tile8==2 and tile9==2) or (tile1==2 and tile4==2 and tile7==2) or (tile2==2 and tile5==2 and tile8==2) or (tile3==2 and tile6==2 and tile9==2) or (tile1==2 and tile5==2 and tile9==2) or (tile3==2 and tile5==2 and tile7==2)):
				return 2
			
			turnchange()
		else:
			return 0

def game1(n):
	
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9

	win1 = 0
	
	for x in range(n):
		tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9 = 0,0,0,0,0,0,0,0,0
		if (game(1) == 1):
			win1+=1

		
			
	return (win1/n)

def game2(n):
	
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn,player1,player2
	win1 = 0
	
	for x in range(n):
		tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9 = 0,0,0,0,0,0,0,0,0
		if (game(2) == 1):
			win1+=1

			
	return (win1/n)

def game3(n):
	
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn,player1,player2
	win1 = 0
	
	for x in range(n):
		tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9 = 0,0,0,0,0,0,0,0,0
		if (game(3) == 1):
			win1+=1
	
	return (win1/n)
