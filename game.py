import pygame 
import sys


# screen initialization

WIDTH = HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SNAKE')

# colors

GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (50, 50, 50)

# objects

class Snake():
	def __init__(self):
		self.x = 100
		self.y = 100
		self.width = 10
		self.parts = [[self.x, self.y]]
		self.color = GREEN
		self.direction = 'right'
		self.velocity = 5

	def move_snake(self):
		if self.direction == 'right':
			self.x += self.velocity
		elif self.direction == 'left':
			self.x -= self.velocity
		elif self.direction == 'top':
			self.y -= self.velocity
		elif self.direction == 'buttom':
			self.y += self.velocity

	def draw_snake(self):
		for part in self.parts:
			pygame.draw.rect(SCREEN, self.color, (part[0], part[1], self.width, self.width))


# game variables and settings

clock = pygame.time.Clock()
FPS = 60
run = True

# game logic (functions)

def update_display():
	SCREEN.fill(GREY)
	snake.draw_snake()
	pygame.display.update()

# initiate game
snake = Snake()

# game loop

while run:

	# event handler

	for event in pygame.event.get():

		# close window event

		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			sys.exit()

	# update screen

	clock.tick(FPS)
	update_display()