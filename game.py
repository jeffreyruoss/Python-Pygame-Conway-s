#!/usr/local/lib/
import pygame
from constants import *
from utilities import *
import cells

class Game(object):
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Jeff\'s Version of Conway\'s Game of Life')
		pygame.time.Clock()
		self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
		self.simulation_running = False
		self.mouse_button_up = False
		self.allsprites = pygame.sprite.Group()

	def mouse_is_inside_live_area(self):
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		if x >= 0 + Constants.MARGIN / 2 and \
			 x <= Constants.LIVE_AREA_SIZE[0] + Constants.MARGIN / 2 and \
			 y >= 0 + Constants.MARGIN / 2 and \
			 y <= Constants.LIVE_AREA_SIZE[1] + Constants.MARGIN / 2: 
			return True
		return False

	def staging(self):
		self.all_cells = cells.AllCells(game)

	def main(self):
		clock = pygame.time.Clock()

		# Staging
		self.staging()
		self.all_cells.staging(game)

		while True:
			clock.tick(30)

			# Events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					return
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					self.simulation_running = True
				if event.type == pygame.MOUSEBUTTONUP and self.simulation_running == False and self.mouse_is_inside_live_area():
					self.mouse_button_up = True

			# Clear
			self.screen.fill((230, 230, 230))
			self.allsprites.clear(self.screen, self.screen)

			# Update
			self.allsprites.update(self)

			# Draw
			self.allsprites.draw(self.screen)

			pygame.display.flip()


game = Game()
game.main()
