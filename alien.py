import pygame
from pygame.sprite import Sprite

#Pygames treats elements as rectangles

class Alien(Sprite):
	"""A class to represent a single alien in the fleet"""

	def __init__(self, ai_game):
		#Gives reference to current instance and self reference
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		#Load image and get its rect.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the aliens horizontal position
		self.x = float(self.rect.x)

	def update(self):
		"""Move the alien to the right."""
		self.x += (self.settings.alien_speed *
						self.settings.fleet_direction)

		self.rect.x = self.x 

	def check_edges(self):
		"""return ture if alien at the edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
