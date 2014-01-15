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
		if self.test == True:
			self.num_neighbors = 0
			for cell in AllCells.cell_list:
				if cell.ID != self.ID and cell.image == Constants.CELL_ALIVE and self.image == Constants.CELL_ALIVE: #if cell is not the same and is alive
					if self.rect.top == cell.rect.bottom and self.rect.left == cell.rect.right:
						print 'cell ', self.ID, 'has a neighbor to the top-left'
						self.num_neighbors += 1
					if self.rect.top == cell.rect.bottom and self.rect.left == cell.rect.left:
						print 'cell ', self.ID, 'has a neighbor to the top'
						self.num_neighbors += 1
					if self.rect.top == cell.rect.bottom and self.rect.right == cell.rect.left:
						print 'cell ', self.ID, 'has a neighbor to the top-right'
						self.num_neighbors += 1
					if self.rect.right == cell.rect.left and self.rect.top == cell.rect.top:
						print 'cell ', self.ID, 'has a neighbor to the right'
						self.num_neighbors += 1
					if self.rect.right == cell.rect.left and self.rect.bottom == cell.rect.top:
						print 'cell ', self.ID, 'has a neighbor to the bottom-right'
						self.num_neighbors += 1
					if self.rect.bottom == cell.rect.top and self.rect.right == cell.rect.right:
						print 'cell ', self.ID, 'has a neighbor to the bottom'
						self.num_neighbors += 1
					if self.rect.bottom == cell.rect.top and self.rect.left == cell.rect.right:
						print 'cell ', self.ID, 'has a neighbor to the bottom-left'
						self.num_neighbors += 1
					if self.rect.left == cell.rect.right and self.rect.top == cell.rect.top:
						print 'cell ', self.ID, 'has a neighbor to the left'
						self.num_neighbors += 1
			print self.ID, 'has', self.num_neighbors, 'neighbors'
			self.test = False