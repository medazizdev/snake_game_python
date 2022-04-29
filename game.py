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
		self.width = 5
		self.parts = [[self.x, self.y], [self.x-self.width, self.y], [self.x-2*self.width, self.y], [self.x-3*self.width, self.y], [self.x-4*self.width, self.y], [self.x-5*self.width, self.y], [self.x-6*self.width, self.y]]
		self.color = GREEN
		self.direction = 'right'
		self.velocity = 5
		print(f'new head coordinate [{self.x}, {self.y}]')
		print(f'\t{self.parts}\n')

	def change_snake_head_coordinates(self):
		if self.direction == 'right':
			self.x += self.velocity
		elif self.direction == 'left':
			self.x -= self.velocity
		elif self.direction == 'up':
			self.y -= self.velocity
		elif self.direction == 'down':
			self.y += self.velocity

		print(f'\nnew head coordinate [{self.x}, {self.y}]')
		

		return [self.x, self.y]

	def change_snake_body_coordinates(self):

		# this solution is not the best -- the velocity should always have the same value as the snake single part width --
		self.parts.pop(-1)
		self.parts.insert(0, self.change_snake_head_coordinates())
		print(f'\t{self.parts}\n')
		

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
	snake.change_snake_body_coordinates()
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

		# game controles

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				snake.direction = 'right'
			if event.key == pygame.K_LEFT:
				snake.direction = 'left'
			if event.key == pygame.K_UP:
				snake.direction = 'up'
			if event.key == pygame.K_DOWN:
				snake.direction = 'down'


	# update screen

	clock.tick(FPS)
	update_display()