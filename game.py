import pygame 
import sys
import random
import math


# screen initialization

WIDTH = HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SNAKE')

# colors

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
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
		self.score = 0
		self.lost = False
		# print(f'new head coordinate [{self.x}, {self.y}]')
		# print(f'\t{self.parts}\n')

	def change_snake_head_coordinates(self):
		if self.direction == 'right':
			self.x += self.velocity
		elif self.direction == 'left':
			self.x -= self.velocity
		elif self.direction == 'up':
			self.y -= self.velocity
		elif self.direction == 'down':
			self.y += self.velocity

		# print(f'\nnew head coordinate [{self.x}, {self.y}]')

		if self.x <= 0:
			self.x = 400
		if self.x > 400:
			self.x = 0
		if self.y <= 0:
			self.y = 400
		if self.y > 400:
			self.y = 0		
		

		return [self.x, self.y]

	def change_snake_body_coordinates(self):

		# this solution is not the best -- the velocity should always have the same value as the snake single part width --
		if not self.lost:
			self.parts.pop(-1)
			self.parts.insert(0, self.change_snake_head_coordinates())
		# print(f'\t{self.parts}\n')

	def check_snake_own_collision(self):
		snake_head_rect = pygame.Rect(self.x, self.y, self.width, self.width)
		for i in range(2, len(self.parts)-1):
			snake_part_rect = pygame.Rect(self.parts[i][0], self.parts[i][1], self.width, self.width)
			if snake_head_rect.colliderect(snake_part_rect):
				self.lost = True
				print('lost')

	def add_score(self):
		x3, y3 = self.parts[-1][0], self.parts[-1][1]
		x2, y2 = self.parts[-2][0], self.parts[-2][1]
		# x1, y1 = self.parts[-3][0], self.parts[-3][1]

		if x3 == x2 and y3 < y2:
			# up
			self.parts.append([x3, y3-self.width])
		if x3 == x2 and y3 > y2:
			# down
			self.parts.append([x3, y3+self.width])
		if x3 < x2 and y3 == y2:
			# left
			self.parts.append([x3-self.width, y3])
		if x3 > x2 and y3 == y2:
			# right
			self.parts.append([x3-self.width, y3])

		self.score += 1

	def draw_snake(self):
		for part in self.parts:
			pygame.draw.rect(SCREEN, self.color, (part[0], part[1], self.width, self.width))


class Apple():
	def __init__(self):
		self.width = 5
		self.color = RED
		self.x = 300
		self.y = 300
		self.apple_rect = pygame.Rect(self.x, self.y, self.width, self.width)

	def change_position(self):
		self.apple_rect.x = random.randrange(10, 390, 5)
		self.apple_rect.y = random.randrange(10, 390, 5)

	def check_eaten(self, snake):
		snake_rect = pygame.Rect(snake.x, snake.y, snake.width, snake.width)
		if snake_rect.colliderect(self.apple_rect):
			self.change_position()
			return True
		return False

	def draw_apple(self):
		pygame.draw.rect(SCREEN, RED, self.apple_rect)


# game variables and settings

clock = pygame.time.Clock()
FPS = 60
run = True

# game logic (functions)

def display_score():
	font = pygame.font.Font('freesansbold.ttf', 14)
	score_text = font.render(str(snake.score), True, BLUE)
	score_text_rect = score_text.get_rect()
	score_text_rect.center = (380, 20)
	SCREEN.blit(score_text, score_text_rect)

def display_timer():
	font = pygame.font.Font('freesansbold.ttf', 14)
	timer_text = font.render(f'{str(math.trunc(pygame.time.get_ticks()/1000))}', True, BLUE)
	timer_text_rect = timer_text.get_rect()
	timer_text_rect.center = (20, 20)
	SCREEN.blit(timer_text, timer_text_rect)


def update_display():
	SCREEN.fill(GREY)
	snake.change_snake_body_coordinates()
	if apple.check_eaten(snake):
		snake.add_score()
	snake.check_snake_own_collision()
	snake.draw_snake()
	apple.draw_apple()
	display_score()
	display_timer()
	pygame.display.update()


# initiate game
pygame.init()
pygame.font.init()
snake = Snake()
apple = Apple()

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
			if event.key == pygame.K_RIGHT and snake.direction != 'left':
				snake.direction = 'right'
			if event.key == pygame.K_LEFT and snake.direction != 'right':
				snake.direction = 'left'
			if event.key == pygame.K_UP and snake.direction != 'down':
				snake.direction = 'up'
			if event.key == pygame.K_DOWN and snake.direction != 'up':
				snake.direction = 'down'
			if event.key == pygame.K_SPACE:
				# print(f'\n{snake.parts}\n\tx head {snake.x} y head {snake.y}\n\tdirection {snake.direction}')
				snake.add_score()

	# update screen

	clock.tick(FPS)
	update_display()