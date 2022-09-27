import pygame, sys

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption("JANKES RUN") #name



icon = pygame.image.load('bear.png')
pygame.display.set_icon(icon) # logo/icon

screen = pygame.display.set_mode((920,400)) #,pygame.FULLSCREEN) #size of frame

banimg = pygame.image.load('banana.png')

background_image = pygame.image.load("background.png").convert()

playerimg = pygame.image.load('monkey.png')
playerx = 5
playery = 425  # player date
playerX_change = 0
playerY_change = 0

def player():
    screen.blit(playerimg, (playerx, playery))

font1 = pygame.font.SysFont(None, 50)
font2 = pygame.font.SysFont(None, 30)






def main_menu():
    while True:

        screen.blit(pygame.image.load("MAIN MENU.png").convert(), [-1, 0])


        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(350, 180, 200, 50)
        button_2 = pygame.Rect(350, 270, 200, 50)
        if button_1.collidepoint((mx, my)) and click:
            game()
        if button_2.collidepoint((mx, my)) and click:
            about()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((74, 224, 191))

        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)

        draw_text('GAME', font1, (255, 255, 255), screen, 420, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == K_ESCAPE:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)


def about():
    running = True
    while running:
        screen.fill((74, 224, 191))

        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)

        draw_text('ABOUT', font1, (255, 255, 255), screen, 420, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == K_ESCAPE:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)

main_menu()


