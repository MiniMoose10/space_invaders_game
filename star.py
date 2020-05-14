import pygame
from pygame.sprite import Sprite

class Star(Sprite):

	def __init__(self, ai_game):
		#Gives reference to current instance and self reference
		super().__init__()
		self.settings = ai_game.settings

		#Load image and get its rect.
		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()

		#Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the aliens horizontal position
		self.x = float(self.rect.x)

