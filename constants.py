import pygame

class Constants:
	LIVE_AREA_SIZE = [400, 400] # The size of the area that the block live
	INFO_UI_HEIGHT = 100
	MARGIN = 50
	SCREEN_SIZE = [LIVE_AREA_SIZE[0] + MARGIN, LIVE_AREA_SIZE[1] + INFO_UI_HEIGHT + MARGIN]
	ROWS = 5
	COLS = 5
	CELL_WIDTH = LIVE_AREA_SIZE[0] / COLS
	CELL_HEIGHT = LIVE_AREA_SIZE[1] / ROWS
	CELL_SIZE = [CELL_WIDTH, CELL_HEIGHT]
	CELL_ALIVE = pygame.transform.scale(pygame.image.load('cell_alive.png'), (CELL_SIZE))
	CELL_DEAD = pygame.transform.scale(pygame.image.load('cell_dead.png'), (CELL_SIZE))