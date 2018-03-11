import pygame

class Ship():
	""" Class to represent the player's ship """
	def __init__(self, screen):
		""" Init the ship and it's starting position """
		self.screen = screen
		
		# Load the ship image get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):
		""" Draw the ship at it's current location """
		self.screen.blit(self.image, self.rect)