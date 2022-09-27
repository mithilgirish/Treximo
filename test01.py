import pygame,sys
import os
from pygame.locals import *
mainClock = pygame.time.Clock()
pygame.init()

pygame.display.set_caption("Jankes RUN") #name

programIcon = pygame.image.load('logo_jankesRun_C.png')
pygame.display.set_icon(programIcon)# logo/icon

display_siz = (pygame.display.Info().current_w, pygame.display.Info().current_h)#display size

screen = pygame.display.set_mode((2256,1504), pygame.RESIZABLE)#3:2
background_image = pygame.image.load(os.path.join('bj', "background2256X1504.png")).convert()
main_image = pygame.image.load(os.path.join('MAINMENU', "MAINMENU2256X1504.png")).convert()
button_1 = pygame.Rect(785, 608, 681, 160)
button_2 = pygame.Rect(785, 848, 681, 160)
button_3 = pygame.Rect(785, 1080, 681, 160)

font1 = pygame.font.SysFont(None, 50)
font2 = pygame.font.SysFont(None, 30)

def main_menu():
    while True:

        screen.blit(main_image, [0, 0])

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)


        mx, my = pygame.mouse.get_pos()


        if button_1.collidepoint((mx, my)) and click:
            game()
        if button_2.collidepoint((mx, my)) and click:
            about()
        if button_3.collidepoint((mx,my)) and click:
            pygame.quit()
            sys.exit()



        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
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
        screen.blit(background_image, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


            print(display_siz)

        pygame.display.update()

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
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

main_menu()





