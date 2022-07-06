import pygame
import random
import textwrap
import os

pygame.init()
sizex = 1200
sizey = 630
os.environ['SDL_VIDEO_WINDOW_POS'] = "40, 40"
win = pygame.display.set_mode((sizex, sizey))

pygame.display.set_caption("ITGS IA")

TempQdatabase = ['A persistent collection of data which is held together in an organised or logical way', 'A single item of data about a person or thing e.g. name date of birth length', 'A set of fields defined to contain information about one thing. e.g. an employee.', 'All of the records regarding a set of people or things', 'An attribute in one table that is a primary key in another table.', 'Indicates the type of data that can be stored in the field', 'User process of checking that the data entered is accurate', 'Validation technique. Requires a field to be completed', 'Verification technique. Two users enter the same data it is then compared for accuracy. Errors are re-entered', 'Verification technique. Someone checking the data entered against the original document', 'A database object which enables you to locate multiple records matching specified criteria' ,'A network of interconnected devices, using telecommunications line, using standardised communication protocols', 'The multimedia content hosted on the devices connected to the Internet.', 'A device that converts analogue signals from telecommunications systems to digital signals for use in computing devices, and vice versa.', 'A device for forwarding data packets to the correct location in a computer network.', 'A specialised computer that manages access to a centralised resource in a network, such as email, media or data files.', 'A device for entering commands or data into a computer system and displays the output. Often used to manage servers.', 'Connects devices in a network. An input to any port is repeated to all ports except the original source port.', 'Connects devices in a network. An input to any port is only send to the device the data packet was addressed to.', 'A network which only covers a small geographical area, such as a building.', 'A network that covers a broad area i.e., links across metropolitan, regional, national or international boundaries']
TempAdatabase = ['database', 'field', 'record', 'table', 'foreign key', 'data type', 'verification', 'presence check', 'double entry', 'proofreading', 'query', 'Internet', 'World Wide Web', 'Modem', 'Router', 'Server', 'Terminal', 'Hub', 'Switch', 'LAN', 'WAN']

Qdatabase = ['A persistent collection of data which is held together in an organised or logical way', 'A single item of data about a person or thing e.g. name date of birth length', 'A set of fields defined to contain information about one thing. e.g. an employee.', 'All of the records regarding a set of people or things', 'An attribute in one table that is a primary key in another table.', 'Indicates the type of data that can be stored in the field', 'User process of checking that the data entered is accurate', 'Validation technique. Requires a field to be completed', 'Verification technique. Two users enter the same data it is then compared for accuracy. Errors are re-entered', 'Verification technique. Someone checking the data entered against the original document', 'A database object which enables you to locate multiple records matching specified criteria' ,'A network of interconnected devices, using telecommunications line, using standardised communication protocols', 'The multimedia content hosted on the devices connected to the Internet.', 'A device that converts analogue signals from telecommunications systems to digital signals for use in computing devices, and vice versa.', 'A device for forwarding data packets to the correct location in a computer network.', 'A specialised computer that manages access to a centralised resource in a network, such as email, media or data files.', 'A device for entering commands or data into a computer system and displays the output. Often used to manage servers.', 'Connects devices in a network. An input to any port is repeated to all ports except the original source port.', 'Connects devices in a network. An input to any port is only send to the device the data packet was addressed to.', 'A network which only covers a small geographical area, such as a building.', 'A network that covers a broad area i.e., links across metropolitan, regional, national or international boundaries']
Adatabase = ['database', 'field', 'record', 'table', 'foreign key', 'data type', 'verification', 'presence check', 'double entry', 'proofreading', 'query', 'Internet', 'World Wide Web', 'Modem', 'Router', 'Server', 'Terminal', 'Hub', 'Switch', 'LAN', 'WAN']

Qdatabase2 = ["Convert 8 into binary", "Convert 7 into binary", "Which logic gate outputs 1, only when both inputs are 1?", "Which logic gate outputs 1, only when either one of the inputs are 1?", "Which logic gate outputs 1, when either one or both of the inputs are 1?"]
Adatabase2 = ["1000", "0111", "AND", "XOR", "OR"]

TempQdatabase2 = ["Convert 8 into binary", "Convert 7 into binary", "Which logic gate outputs 1, only when both inputs are 1?", "Which logic gate outputs 1, only when either one of the inputs are 1?", "Which logic gate outputs 1, when either one or both of the inputs are 1?"]
TempAdatabase2 = ["1000", "0111", "AND", "XOR", "OR"]

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png')]
walkUp = [pygame.image.load('U1.png'), pygame.image.load('U2.png'), pygame.image.load('U3.png'), pygame.image.load('U4.png')]
walkDown = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png'), pygame.image.load('D4.png')]
bg = pygame.image.load('bg.jpg')
bg1 = pygame.image.load('bg1.jpg')

pause = True
instruction = True
run = True
run1 = True
run2 = True
jumpStrength = 0
x = 0
score = 0
jumpLimiter = 0
refreshrateblock = 0
answerrange = 0
difficultylevel = 0
clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
    	global jumpStrength
    	self.x = x
    	self.y = y
    	self.width = width
    	self.height = height
    	self.vel = 5
    	self.left = False
    	self.right = False
    	self.up = False
    	self.down = False
    	self.walkCount = 0
    	self.standing = True
    	self.hitbox = (self.x+13, self.y, 74, 100)
    	self.isJump = False
    	self.jumpCount = jumpStrength

    def draw(self,win):
        if self.walkCount >= 36:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//9], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//9], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(walkDown[self.walkCount//9], (self.x, self.y))
                self.walkCount += 1
            elif self.up:
                win.blit(walkUp[self.walkCount//9], (self.x, self.y))
                self.walkCount += 1
        else:
        	win.blit(walkUp[0], (self.x, self.y))
        	if self.left:
        		win.blit(walkLeft[0], (self.x, self.y))
        	if self.right:
        		win.blit(walkRight[0], (self.x, self.y))
        	if self.down:
        		win.blit(walkDown[0], (self.x, self.y))
        	if self.up:
        		win.blit(walkUp[0], (self.x, self.y))
        self.hitbox = (self.x+13, self.y, 74, 100)     

class questionblock(object):
	def __init__(self, x, y, text, ii):
		self.font = pygame.font.SysFont('Arial', 25)
		self.x = x
		self.y = y
		self.text = text
		self.ii = ii

	def showquestion(self, win):
		win.blit(self.font.render(self.text, True, (0,0,0)), (self.x+3, self.y+20))

class answerblock(object):
	def __init__(self, x, y, width, height, color, text, iii, vel):
		self.font = pygame.font.SysFont('Arial', 25)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel
		self.color = color
		self.text = text
		self.hitbox = (self.x, self.y, self.width, self.height)
		self.iii = iii

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
		win.blit(self.font.render(self.text, True, (0,0,0)), (self.x+3, self.y+self.height/4))
		self.hitbox = (self.x, self.y, self.width, self.height)

class answerblock1(object):
	def __init__(self, x, y, width, height, color, text, iii, vel):
		self.font = pygame.font.SysFont('Arial', 25)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel
		self.color = color
		self.text = text
		self.hitbox = (self.x, self.y, self.width, self.height)
		self.iii = iii

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 2)
		win.blit(self.font.render(self.text, True, (0,0,0)), (self.x+3, self.y+55))
		self.hitbox = (self.x, self.y, self.width, self.height)

def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def writetext(text, font, size, color, x, y):
	largeText = pygame.font.SysFont(font, size)
	TextSurf, TextRect = text_objects(text, largeText, color)
	TextRect = (x,y)
	win.blit(TextSurf, TextRect)

def button(msg,x,y,w,h,ic,ac,size,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(win, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("arial",size)
    textSurf, textRect = text_objects(msg, smallText, (0,0,0))
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)

def difficulty():
	global run1
	pygame.draw.rect(win, (255,140,0) , (sizex/2-475,80,950,480))
	largeText = pygame.font.SysFont("comicsans", 80)
	TextSurf, TextRect = text_objects("Choose difficulty", largeText, (0,0,0))
	TextRect.center = ((sizex/2),(190))
	win.blit(TextSurf, TextRect)

	run1=True
	while run1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	                
		button("Easy",sizex/2-170/2-200,290,170,60,(0,170,0), (0,120,0), 43, easy)
		button("Medium",sizex/2-170/2,290,170,60,(205,205,0), (160,160,0), 43, medium)
		button("Hard",sizex/2-170/2+200,290,170,60,(230,0,0), (190,0,0), 43, hard)

		pygame.display.update()

def victory():
	global run2
	global score
	global difficultylevel
	largeText = pygame.font.SysFont("comicsans", 80)
	TextSurf, TextRect = text_objects("Congratulations!", largeText, (0,0,0))
	TextRect.center = ((sizex/2),(100))
	win.blit(TextSurf, TextRect)
	largeText1 = pygame.font.SysFont("comicsans", 40)
	TextSurf1, TextRect1 = text_objects("You've answered all questions", largeText1, (0,0,0))
	TextRect1.center = ((sizex/2),(150))
	win.blit(TextSurf1, TextRect1)
	writetext("Your final score was "+str(score)+", achieved at difficulty level "+difficultylevel, "comicsans", 40, (0,0,0), 210, 180)
	run2=True
	while run2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()            
		button("Play again", 244, 240, 250, 100, (0,170,0), (0,120,0), 40, restartgame) #Restart game button
		button("Main menu", 706, 240, 250, 100, (230,0,0), (190,0,0), 40, backtomain1)
		pygame.display.update()

def restartgame():
	global run2
	global score
	global TempQdatabase
	global TempAdatabase
	global Qdatabase
	global Adatabase
	global TempQdatabase2
	global TempAdatabase2
	global Qdatabase2
	global Adatabase2
	score = 0
	run2=False
	Qdatabase = TempQdatabase.copy() #Reset list
	Adatabase = TempAdatabase.copy() #Reset list
	Qdatabase2 = TempQdatabase2.copy() #Reset list
	Adatabase2 = TempAdatabase2.copy() #Reset list

def easy():
	global refreshrateblock
	global run1
	global answerrange
	global jumpStrength
	global jumpLimiter
	global difficultylevel
	refreshrateblock = 90
	answerrange = 3
	jumpStrength = 26
	jumpLimiter = 32
	run1=False
	difficultylevel = "easy"

def medium():
	global jumpLimiter
	global refreshrateblock
	global run1
	global answerrange
	global jumpStrength
	global difficultylevel
	jumpLimiter = 25
	refreshrateblock = 75
	answerrange = 4
	jumpStrength = 23
	run1 = False
	difficultylevel = "medium"

def hard():
	global jumpLimiter
	global refreshrateblock
	global run1
	global answerrange
	global jumpStrength
	global difficultylevel
	jumpLimiter = 11
	refreshrateblock = 60
	answerrange = 5
	jumpStrength = 18
	run1 = False
	difficultylevel = "hard"

def unpause():
	global pause
	pause = False

def backtomain():
	unpause()
	global run
	run=False
	game_intro()

def closevictory():
	global run2
	run2 = False

def backtomain1():
	closevictory()
	global run
	global TempQdatabase
	global TempAdatabase
	global Qdatabase
	global Adatabase
	global TempQdatabase2
	global TempAdatabase2
	global Qdatabase2
	global Adatabase2
	Qdatabase = TempQdatabase.copy()
	Adatabase = TempAdatabase.copy()
	Qdatabase2 = TempQdatabase2.copy()
	Adatabase2 = TempAdatabase2.copy()
	run=False
	game_intro()

def backtomain2():
	global instruction
	instruction = False
	
def paused():
	global pause
	global run
	global bg
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	               
		win.blit(bg, (0,0))
		title = pygame.font.SysFont("comicsans",85)
		TextSurf, TextRect = text_objects("Paused", title, (0,0,0))
		TextRect.center = (sizex/2, 100)
		win.blit(TextSurf, TextRect)
		button("Continue game", 244, 240, 250, 100, (0,170,0), (0,120,0), 40, unpause)
		button("Main menu", 706, 240, 250, 100, (230,0,0), (190,0,0), 40, backtomain)
		pygame.display.update()

def paused1():
	global pause
	global run
	global bg
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	               
		win.blit(bg1, (0,0))
		title = pygame.font.SysFont("comicsans",85)
		TextSurf, TextRect = text_objects("Paused", title, (0,0,0))
		TextRect.center = (sizex/2, 100)
		win.blit(TextSurf, TextRect)
		button("Continue game", 244, 240, 250, 100, (0,170,0), (0,120,0), 40, unpause)
		button("Main menu", 706, 240, 250, 100, (230,0,0), (190,0,0), 40, backtomain)
		pygame.display.update()

def start_instructions():
	global instruction
	instruction = True
	instructions()

def instructions():
	global instruction
	while instruction:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.draw.rect(win, (255,140,0) , (sizex/2-450,80,900,480))
		largeText = pygame.font.SysFont("comicsans", 80)
		TextSurf, TextRect = text_objects("Instructions", largeText, (0,0,0))
		TextRect.center = ((sizex/2),(170))
		win.blit(TextSurf, TextRect)
		button("Main menu",sizex/2-210/2,480,210,60,(230,0,0), (190,0,0), 43, backtomain2)
		writetext("Theory game", "comicsans", 56, (0,0,0), 180, 210)
		writetext("• Move up, left, down, right with the arrow", "arial", 25, (0,0,0), 180, 250)
		writetext("keys or with W, A, S, D", "arial", 25, (0,0,0), 192, 278)
		writetext("• Choose an answer by colliding with a block", "arial", 25, (0,0,0), 180, 310)
		writetext("• Correct answer chosen: +1 points, wrong", "arial", 25, (0,0,0), 180, 342)
		writetext("answer chosen: -1 points", "arial", 25, (0,0,0), 193, 370)
		writetext("• Objective: answer all questions", "arial", 25, (0,0,0), 180, 402)
		writetext("• Press 'P' to pause", "arial", 25, (0,0,0), 180, 434)
		writetext("Logic game", "comicsans", 56, (0,0,0), 610, 210)
		writetext("• Press space to jump", "arial", 25, (0,0,0), 610, 250)
		writetext("• Choose an answer by colliding with a block", "arial", 25, (0,0,0), 610, 282)
		writetext("• Correct answer chosen: +1 points, wrong", "arial", 25, (0,0,0), 610, 314)
		writetext("answer chosen: -1 points", "arial", 25, (0,0,0), 623, 342)
		writetext("• Objective: answer all questions", "arial", 25, (0,0,0), 610, 374)
		writetext("• Press 'P' to pause", "arial", 25, (0,0,0), 610, 406)
		pygame.display.update()

def game_intro():
	global run
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
        
		win.fill((50,100,50))
		title = pygame.font.SysFont("comicsans",85)
		TextSurf, TextRect = text_objects("Computer Science Revision Game", title, (0,190,0))
		TextRect.center = (sizex/2, 200)
		win.blit(TextSurf, TextRect)
		button("Theory Game", 144, 375, 250, 100, (0,170,0), (0,120,0), 40, rungame1_loop)
		button("Logic Game", sizex/2-125, 375, 250, 100, (0,170,0), (0,120,0), 40, rungame2_loop)
		button("Instructions", 806, 375, 250, 100, (0,170,0), (0,120,0), 40, start_instructions)
		button("Quit game", sizex-125, 25, 100, 50, (230,0,0), (190,0,0), 20, quitgame)
		pygame.display.update()

def rungame1_loop():
	difficulty()
	global run
	run = True
	game1_loop()

def game1_loop():
	global pause
	global run
	global refreshrateblock
	global answerrange
	global score
	def redrawGameWindow():
		win.blit(bg, (0,0))
		man.draw(win)
		font = pygame.font.SysFont("comicsans",40)
		for block in blocks:
			block.draw(win)
		for question in questions:
			question.showquestion(win)
		TextSurf, TextRect = text_objects("Score: "+str(score), font, (0,0,0))
		TextRect.center = (1130, 25)
		win.blit(TextSurf, TextRect)
		pygame.display.update()

	man = player(sizex/2-50, 510, 100, 100)
	timegap=1
	show = 0
	questions=[]
	blocks=[]
	score=0
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		clock.tick(36)

		if timegap > 0:
			timegap += 1
		if timegap > refreshrateblock:
			timegap = 0

		for block in blocks:
			if man.hitbox[1] < block.hitbox[1] + block.hitbox[3] and man.hitbox[1] + man.hitbox[3] > block.hitbox[1]:
				if man.hitbox[0] + man.hitbox[2] > block.hitbox[0] and man.hitbox[0] < block.hitbox[0] + block.hitbox[2]:
					if ii == block.iii: #if right answer chosen
						questions.clear()
						show=0
						man.x= sizex/2-50
						man.y= 460
						blocks.clear()
						score+=1
						if len(Qdatabase) > 1:
							Qdatabase.pop(ii)
							Adatabase.pop(ii)
						else:
							victory()

					elif ii != block.iii: #if wrong answer chosen
						questions.clear()
						show=0
						man.x= sizex/2-50
						man.y= 460
						blocks.clear()
						score-=1



			if block.y < sizey:
				block.y += block.vel
			else:
				blocks.pop(blocks.index(block))

		if show==0:
			ii = random.randint(0, len(Qdatabase)-1)
			text= Qdatabase[ii]
			questions.append(questionblock(20, 20, text, ii))
			show+=1

		if len(blocks) < 5 and timegap ==0:
			if len(Qdatabase) > answerrange:
				if ii>=answerrange and ii<=len(Qdatabase)-answerrange:
					iii = random.randint(ii-(answerrange-2), ii+(answerrange-2))
				elif ii<answerrange:
					iii = random.randint(0, answerrange-1)
				else:
					iii = random.randint(ii-answerrange+1, len(Qdatabase)-1)
			else:
				iii = random.randint(0, len(Qdatabase)-1)
			
			broken = textwrap.wrap(Adatabase[iii], width=21)
			XPOS= random.uniform(0,sizex-200)
			R = random.uniform(170,255)
			G = random.uniform(170,255)
			B = random.uniform(170,255)
			if len(broken) == 1:
				blocks.append(answerblock(XPOS, -100, 200, 100, (R,G,B), broken[0], iii, answerrange))
			else:
				blocks.append(answerblock(XPOS, -100, 200, 100, (R,G,B), broken[0], iii, answerrange))
				blocks.append(answerblock1(XPOS, -100, 199, 80, (R,G,B), broken[1], iii, answerrange))
			timegap = 1

		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > 0:
			man.x -= man.vel
			man.left = True
			man.right = False
			man.up = False
			man.down = False
			man.standing = False
		elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < sizex - man.width:
			man.x += man.vel
			man.left = False
			man.right = True
			man.up = False
			man.down = False
			man.standing = False
		elif keys[pygame.K_UP] or keys[pygame.K_w] and man.y > 0:
			man.y -= man.vel
			man.left = False
			man.right = False
			man.up = True
			man.down = False
			man.standing = False
		elif keys[pygame.K_DOWN] or keys[pygame.K_s] and man.y < sizey - man.height:	
			man.y += man.vel
			man.left = False
			man.right = False
			man.up = False
			man.down = True
			man.standing = False
		else:
			man.standing = True

		if keys[pygame.K_p]:
			pause = True
			paused()
		
		redrawGameWindow()

def rungame2_loop():
	difficulty()
	global run
	run = True
	game2_loop()

def game2_loop():
	global pause
	global run
	global jumpLimiter
	global refreshrateblock
	global answerrange
	global x
	global score
	global jumpStrength
	def redrawGameWindow():
		man.draw(win)
		font = pygame.font.SysFont("comicsans",40)
		for block in blocks:
			block.draw(win)
		for question in questions:
			question.showquestion(win)
		TextSurf, TextRect = text_objects("Score: "+str(score), font, (0,0,0))
		TextRect.center = (1130, 25)
		win.blit(TextSurf, TextRect)
		pygame.display.update()

	man = player(sizex/2-50, 460, 100, 100)
	timegap=1
	show = 0
	questions=[]
	blocks=[]
	score=0
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		clock.tick(36)

		rel_x = x % 1200
		win.blit(bg1, (rel_x - 1200, 0))
		if rel_x < 1200:
			win.blit(bg1, (rel_x, 0))
		x -= (answerrange+2)*(answerrange+2)*0.4

		if timegap > 0:
			timegap += 1
		if timegap > refreshrateblock-20:
			timegap = 0

		for block in blocks:
			if man.hitbox[1] < block.hitbox[1] + block.hitbox[3] and man.hitbox[1] + man.hitbox[3] > block.hitbox[1]:
				if man.hitbox[0] + man.hitbox[2] > block.hitbox[0] and man.hitbox[0] < block.hitbox[0] + block.hitbox[2]:
					if ii == block.iii: #if right answer chosen
						man.x= 550
						man.y= 460
						questions.clear()
						show=0
						blocks.clear()
						score+=1
						if len(Qdatabase2) > 1: #If there are more than 1 questions in the list
							Qdatabase2.pop(ii)
							Adatabase2.pop(ii)
						else: #If there is one or less questions remaining in the list
							victory() #Run victory

					elif ii != block.iii: #if wrong answer chosen
						man.x = 550
						man.y = 460
						questions.clear()
						show = 0
						blocks.clear()
						score-=1

			if block.x > -120:
				block.x -= block.vel
			else:
				blocks.pop(blocks.index(block))

		if show==0:
			ii = random.randint(0, len(Qdatabase2)-1)
			
			text= Qdatabase2[ii]
			questions.append(questionblock(20, 20, text, ii))
			show+=1

		if len(blocks) < 5 and timegap ==0:
			if len(Qdatabase2) > answerrange:
				if ii>=answerrange and ii<=len(Qdatabase2)-answerrange:
					iii = random.randint(ii-(answerrange-2), ii+(answerrange-2))
				elif ii<answerrange:
					iii = random.randint(0, answerrange-1)
				else:
					iii = random.randint(ii-answerrange+1, len(Qdatabase2)-1)
			else:
				iii = random.randint(0, len(Qdatabase2)-1)
			
			

			R = random.uniform(170,255)
			G = random.uniform(170,255)
			B = random.uniform(170,255)
			blocks.append(answerblock(1350, 510, 100, 50, (R,G,B), Adatabase2[iii], iii, (answerrange+2)*(answerrange+2)*0.4))

			timegap = 1

		keys = pygame.key.get_pressed()

		man.standing = False
		man.left = False
		man.right = True
		man.up = False
		man.down = False
		
		if not(man.isJump):
			if keys[pygame.K_SPACE]:	
				man.isJump = True
		else:
			if man.jumpCount >= -jumpStrength:
				neg = 1
				if man.jumpCount < 0:
					neg = -1
				man.y -= man.jumpCount ** 2 *neg/jumpLimiter
				man.jumpCount -= 1
			else:
				man.isJump = False
				man.jumpCount = jumpStrength
		if man.y>460:
			man.y=460
		
		if keys[pygame.K_p]:
			pause = True
			paused1()

		redrawGameWindow()

game_intro()
pygame.quit()
quit()
