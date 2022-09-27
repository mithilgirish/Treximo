import pygame
pygame.init()

pygame.display.set_caption("BABA JankeS") #name



screen = pygame.display.set_mode((1600,900)) #size of frame



background_image = pygame.image.load("background1.png").convert()

playerimg = pygame.image.load('monkey.png')
playerx = 5
playery = 425 #player date
playerX_change = 0
playerY_change = 0



def player():
    screen.blit(playerimg,(playerx,playery))




running = True
while running:

    #screen.blit(background_image, [0, 0])
    screen.fill((255, 0, 40))  # screen color
    #screen.blit(background_image, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerY_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    #block for X axis
    if playerx >= 5:
        playerx += playerX_change
    elif playerx <= 5:
         playerx = 5

    if playerx <= 1920:
        playerx += playerX_change
    elif playerx >= 1920:
         playerx = 1920
    #########################

    #block for Y axis
    if playery >= 5:
        playery += playerY_change
    elif playery <= 5:
         playery = 5

    if playery <= 425:
        playery += playerY_change
    elif playery >= 425:
         playery = 425
    ##########################

    player()
    ###############################################
    #test

    print ("x value", playerx)

    print ("y value",playery)

    ###############################################

    pygame.display.update()
