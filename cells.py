import pygame
from constants import *

class AllCells(object):
	cell_list = []
	ID = 0
	def __init__(self, game):
		pass

	def staging(self, game):
		self.create_cells(game)

	def create_cells(self, game):
		rows, cols = Constants.ROWS, Constants.COLS
		x = 0 + Constants.MARGIN / 2
		y = 0 + Constants.MARGIN / 2

		for row in xrange(rows):
			for col in xrange(cols):
				Cell(game, x, y)
				x += Constants.CELL_WIDTH
			x = 0 + Constants.MARGIN / 2
			y += Constants.CELL_HEIGHT
		

class Cell(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		self.test = True
		self.ID = AllCells.ID
		AllCells.ID += 1
		self.x = x
		self.y = y
		self.image = Constants.CELL_DEAD
		self.rect = pygame.rect.Rect((self.x, self.y), Constants.CELL_SIZE)
		self.num_neighbors = 0
		pygame.sprite.Sprite.__init__(self, game.allsprites)
		AllCells.cell_list.append(self)

	def update(self, game):
		self.click_activate_deactivate(game)

		if game.simulation_running == True:
			self.count_live_neighbors(game)

	def click_activate_deactivate(self, game):
		if self.rect.collidepoint(pygame.mouse.get_pos()) and game.mouse_button_up == True:
			if self.image == Constants.CELL_DEAD:
				self.image = Constants.CELL_ALIVE
			else:
				self.image = Constants.CELL_DEAD
			game.mouse_button_up = False

	def count_live_neighbors(self, game):
		self.num_neighbors = 0
		for cell in AllCells.cell_list:
			if cell.ID != self.ID and cell.image == Constants.CELL_ALIVE: # not comparing against itself and the cell to check is alive
				if cell.rect.bottom == self.rect.top and cell.rect.right == self.rect.left: # if it has a top left corner neighbor
					self.num_neighbors += 1
				if cell.rect.bottom == self.rect.top and cell.rect.left == self.rect.left: # if it has a top neighbor
					self.num_neighbors += 1
		if self.test == True:
			print 'self.ID: ', self.ID, ' - cell.ID: ', cell.ID, ' - num_neighbors: ', self.num_neighbors
			self.test = False

