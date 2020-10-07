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
yellow_Ship = pygame.image.load(os.path.join('assests' , 'ship_yellow.png'))

# Lasers
red_laser = pygame.image.load(os.path.join('assests' , 'laser_red.png'))
blue_laser = pygame.image.load(os.path.join('assests' , 'laser_blue.png'))
green_laser = pygame.image.load(os.path.join('assests' , 'laser_red.png'))
yellow_laser = pygame.image.load(os.path.join('assests' , 'laser_yellow.png'))

# Background
bg = pygame.transform.scale (pygame.image.load(os.path.join('assests' , 'background-black.png')) , (win_width, win_Height) )


# Laser class
class Laser :
    def __init__(self , x , y , img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw (self , window):
        window.blit(self.img , (self.x , self.y))

    def move (self , vel):
        self.y += vel

    def off_screen (self , height):
        return self.y <= height and self.y >= 0

    def colloision(self , obj):
        return isCollide (obj , self)

# Ship class
class Ship :
    def __init__ (self , x , y , health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw (self , window ):
        # pygame.draw.rect(window, (255,0,0) ,(self.x , self.y , 50 ,50 ))
        window.blit(self.ship_img, (self.x, self.y))

    def get_width (self):
        return self.ship_img.get_width()


    def get_height (self):
        return self.ship_img.get_height()

# Player class
class Player (Ship):
    def __init__(self , x ,y , health=100):
        super().__init__(x , y , health)
        self.ship_img = yellow_Ship
        self.laser_img = yellow_laser
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

# Enemy class
class Enemy(Ship):
    def __init__(self , x , y , health , color):
        super().__init__(x , y , health)
        self.ship_img , self.laser_img = self.color_map[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    color_map = {
                "red" : (red_Ship, red_laser),
                "green" : (green_Ship, green_laser),
                "blue" : (blue_Ship, blue_laser)
                }
                
    def move (self , vel):
        self.y += vel


def isCollide ()

# Main Loop
def main():
    run = True
    framePerSeconds = 60
    clock = pygame.time.Clock()
    level = 0
    lives = 5

    # Player
    player = Player(300 , 200)
    player_vel = 5
    main_font = pygame.font.SysFont('comicsans', 40, italic=True)
    lost_font = pygame.font.SysFont('comicsans', 60, bold=True , italic=True)

    # Enemies
    enemies = []
    wave_length = 5 
    enemies_vel = 15

    lost = False
    lost_count = 0


    def redraw ():
        win.blit(bg , (0,2))
        
        for enemy in enemies :
            enemy.draw(win)
        player.draw(win)

        if lost :
            lost_lable = lost_font.render("You Lost" , 1 , (255,255,255))
            win.blit(lost_lable , (win_width/2 - lost_lable.get_width()/2  , 350 ))
        
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

        if lives <= 0 or player.health <= 0 : 
            lost = True
            lost_count +=1

        if lost :
            if lost_count > framePerSeconds * 2:
                run = False
            else :
                continue
        
        if len(enemies) == 0 :
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50 , win_width-100), random.randrange(-1500  , -100) , 100 , random.choice(["red" , "blue" , "green"]) )
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False

        keys = pygame.key.get_pressed()

        if keys [pygame.K_d] and player.x + player_vel + player.get_width() < win_width : # right
            player.x += player_vel

            
        if keys [pygame.K_a] and player.x - player_vel > 0 : # left
            player.x -= player_vel


        if keys [pygame.K_w] and player.y - player_vel > 0 : # up
            player.y -= player_vel


        if keys [pygame.K_s] and player.y + player_vel + player.get_height() < win_Height : # down
            player.y += player_vel

        for enemy in enemies[:] :
            enemy.move(enemies_vel)
            if enemy.y + enemy.get_height () > win_Height :
                lives -=1
                enemies.remove(enemy)

        

main()