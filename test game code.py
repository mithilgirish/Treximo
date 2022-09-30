import pygame
import os

pygame.init()
win = pygame.display.set_mode((1920, 1080))
bg_img = pygame.image.load(os.path.join("Background","4.png"))
bg = pygame.transform.scale(bg_img, (1920, 1080))

width = 1920
i = 0

player1=[pygame.image.load(os.path.join("players",'1_run0.png')),
         pygame.image.load(os.path.join("players",'1_run0.png')),
         pygame.image.load(os.path.join("players",'1_run0.png')),
         pygame.image.load(os.path.join("players",'1_run1.png')),
         pygame.image.load(os.path.join("players",'1_run1.png')),
         pygame.image.load(os.path.join("players",'1_run1.png')),
         pygame.image.load(os.path.join("players",'1_run2.png')),
         pygame.image.load(os.path.join("players",'1_run2.png')),
         pygame.image.load(os.path.join("players",'1_run2.png')),
         pygame.image.load(os.path.join("players",'1_jump.png'))]

player2=[pygame.image.load(os.path.join("players",'2_run0.png')),
         pygame.image.load(os.path.join("players",'2_run0.png')),
         pygame.image.load(os.path.join("players",'2_run0.png')),
         pygame.image.load(os.path.join("players",'2_run1.png')),
         pygame.image.load(os.path.join("players",'2_run1.png')),
         pygame.image.load(os.path.join("players",'2_run1.png')),
         pygame.image.load(os.path.join("players",'2_run2.png')),
         pygame.image.load(os.path.join("players",'2_run2.png')),
         pygame.image.load(os.path.join("players",'2_run2.png')),
         pygame.image.load(os.path.join("players",'2_jump.png'))]

player3=[pygame.image.load(os.path.join("players",'3_run0.png')),
         pygame.image.load(os.path.join("players",'3_run0.png')),
         pygame.image.load(os.path.join("players",'3_run0.png')),
         pygame.image.load(os.path.join("players",'3_run1.png')),
         pygame.image.load(os.path.join("players",'3_run1.png')),
         pygame.image.load(os.path.join("players",'3_run1.png')),
         pygame.image.load(os.path.join("players",'3_run2.png')),
         pygame.image.load(os.path.join("players",'3_run2.png')),
         pygame.image.load(os.path.join("players",'3_run2.png')),
         pygame.image.load(os.path.join("players",'3_jump.png'))]

player4=[pygame.image.load(os.path.join("players",'4_run0.png')),
         pygame.image.load(os.path.join("players",'4_run0.png')),
         pygame.image.load(os.path.join("players",'4_run0.png')),
         pygame.image.load(os.path.join("players",'4_run1.png')),
         pygame.image.load(os.path.join("players",'4_run1.png')),
         pygame.image.load(os.path.join("players",'4_run1.png')),
         pygame.image.load(os.path.join("players",'4_run2.png')),
         pygame.image.load(os.path.join("players",'4_run2.png')),
         pygame.image.load(os.path.join("players",'4_run2.png')),
         pygame.image.load(os.path.join("players",'4_jump.png'))]
         
n=0
x = width/2
y = 650
vel_x = 10
vel_y = 10
jump = False

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #win.fill((0,0,0))

    #Create looping background
    win.blit(bg, (i, 0))
    win.blit(bg, (width+i, 0))
    if i == -width:
        win.blit(bg, (width+i, 0))
        i = 0
    i -= 12

    
    #player
    
    win.blit(player1[n],(int(x),int(y))) #player1
    #win.blit(player2[n],(int(x),int(y))) #player2
    #win.blit(player3[n],(int(x),int(y))) #player3
    #win.blit(player4[n],(int(x),int(y))) #player4
    
    n = n+1
    if n>=6:
        n=0
    #Jump
    userInput = pygame.key.get_pressed()
    if jump is False and userInput[pygame.K_SPACE]:
        jump = True
    if jump is True:
        n=7
        y -= vel_y*4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    pygame.time.Clock().tick(60)
    pygame.display.update()

"""
import pygame
import os
import random

# Init and Create Window (win)
pygame.init()
win_height = 400
win_width = 800
win = pygame.display.set_mode((win_width, win_height))

# Load and Size Images
# Hero (Player)
left = [pygame.image.load(os.path.join("Assets/Hero", "L1.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L2.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L3.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L4.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L5.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L6.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L7.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L8.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L9.png"))
        ]
right =[pygame.image.load(os.path.join("Assets/Hero", "R1.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R2.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R3.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R4.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R5.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R6.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R7.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R8.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R9.png"))
        ]

# Background
background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Background.png")), (win_width, win_height))



class Hero:
    def __init__(self, x, y):
        # Walk
        self.x = x
        self.y = y
        self.velx = 10
        self.vely = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        # Jump
        self.jump = False
        # Bullet
        self.bullets = []
        self.cool_down_count = 0
        # Health
        self.hitbox = (self.x, self.y, 64, 64)

    def move_hero(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width - 62:
            self.x += self.velx
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    def draw(self, win):
        self.hitbox = (self.x + 15, self.y + 15, 30, 40)
        #pygame.draw.rect(win, (0,0,0), self.hitbox, 1)
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

    def jump_motion(self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vely*4
            self.vely -= 1
        if self.vely < -10:
            self.jump = False
            self.vely = 10

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1



# Draw Game
def draw_game():
    win.fill((0, 0, 0))
    win.blit(background, (0,0))
    player.draw(win)
    pygame.time.delay(30)
    pygame.display.update()

# Instance of Hero-Class
player = Hero(250, 290)

# Instance of Enemy-Class
enemies = []

# Mainloop
run = True
while run:

    # Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Input
    userInput = pygame.key.get_pressed()


    # Movement
    player.move_hero(userInput)
    player.jump_motion(userInput)

    

    # Draw Game in Window
    draw_game()
"""
