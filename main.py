# Space invedres using pygame

import pygame
import os
import time
import random

# Setting the font
pygame.font.init()

# Setting the game's window
win_width , win_Height = 1000 , 690
win = pygame.display.set_mode((win_width , win_Height))
pygame.display.set_caption('Space Shooter')

# Load images
red_Ship = pygame.image.load(os.path.join('assests' , 'ship_red_small.png'))
blue_Ship = pygame.image.load(os.path.join('assests' , 'ship_blue_small.png'))
green_Ship = pygame.image.load(os.path.join('assests' , 'ship_green_small.png'))

# Main player
Yellow_Ship = pygame.image.load(os.path.join('assests' , 'ship_yellow.png'))

# Lasers
red_laser = pygame.image.load(os.path.join('assests' , 'laser_red.png'))
blue_laser = pygame.image.load(os.path.join('assests' , 'laser_blue.png'))
green_laser = pygame.image.load(os.path.join('assests' , 'laser_red.png'))
yellow_laser = pygame.image.load(os.path.join('assests' , 'laser_yellow.png'))

# Background
bg = pygame.transform.scale (pygame.image.load(os.path.join('assests' , 'background-black.png')) , (win_width, win_Height) )

# Ship class

class Ship :
    def __init__ (self , x , y , health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers []
        self.cool_down_counter = 0

    def draw (self):
        

        


# Main Loop
def main():
    run = True
    framePerSeconds = 60
    clock = pygame.time.Clock()
    level = 1 
    lives = 5

    main_font = pygame.font.SysFont('comicsans', 40, italic=True)

    def redraw ():
        win.blit(bg , (0,2))

        # Draw level and lives
        level_lable = main_font.render(f"level : {level}" , 1 , (255,255,255))
        lives_lable = main_font.render(f"lives : {lives}" , 1 , (255,255,255))

        win.blit(level_lable , (10,10))
        # win.blit(lives_lable , (685,10))
        win.blit(lives_lable , (win_width - lives_lable.get_width()-10 ,10))

        # Update the screen
        pygame.display.update()

    while run :
        clock.tick(framePerSeconds)
        redraw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False

main()