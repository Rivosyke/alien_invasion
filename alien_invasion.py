#!/usr/bin/python

import sys
import pygame
from Settings import Settings
from ship import Ship

def run_game():
	# Initialize pygame, settings, and screen object
	pygame.display.init()
	pygame.mixer.quit()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_width))
	pygame.display.set_caption("Alien Invasion")
	bg_color = (230,230,230)
	
	ship = Ship(screen)
	
	while True:
		
		# Watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		
		# Make the most recently drawn screen visible
		pygame.display.flip()
		

run_game()
