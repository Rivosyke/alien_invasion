#!/usr/bin/python

import pygame
from Settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object
	pygame.display.init()
	pygame.mixer.quit()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion!")
	bg_color = ai_settings.bg_color
	
	ship = Ship(ai_settings, screen)
	
	while True:		
		# Watch for keyboard and mouse events
		gf.check_events(ship)	
		ship.update()	
		gf.update_screen(ai_settings, screen, ship)
		
		
run_game()
