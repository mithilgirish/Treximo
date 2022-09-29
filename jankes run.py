import pygame,sys
import os
from pygame.locals import *
mainClock = pygame.time.Clock()
pygame.init()
 
pygame.display.set_caption("CS project") #name

programIcon = pygame.image.load('logo_jankesRun_C.png')
pygame.display.set_icon(programIcon)# logo/icon
 
display_siz = (pygame.display.Info().current_w, pygame.display.Info().current_h)#display size
wi = pygame.display.Info().current_w
he = pygame.display.Info().current_h
clicksound = pygame.mixer.Sound(os.path.join("SFX","click.ogg"))

  
if display_siz == (1366,768):
    screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
    background_image = pygame.image.load(os.path.join('bj',"background1366X768.png")).convert()
    main_image = pygame.image.load(os.path.join('MAINMENU',"MAINMENU1366X768.png")).convert()
    button_1y = 298
    button_2y = 445
    button_3y = 585
    button_x = 490
    button_w = 380
    button_h = 95
    button_1 = pygame.Rect(button_x, button_1y, button_w, button_h)
    button_2 = pygame.Rect(button_x, button_2y, button_w, button_h)
    button_3 = pygame.Rect(button_x,button_3y, button_w, button_h)
    font = pygame.font.Font('Quicksand.ttf', 100)
    font1 = pygame.font.Font('Quicksand.ttf', 50)
    font2 = pygame.font.Font('Quicksand.ttf', 30)
    ts = 30

elif display_siz == (1920,1080):
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    background_image = pygame.image.load(os.path.join('bj', "background1920X1080.png")).convert()
    main_image = pygame.image.load(os.path.join('MAINMENU', "MAINMENU1920X1080.png")).convert()
    button_1y = 418
    button_2y = 622
    button_3y = 819
    button_x = 665
    button_w = 578
    button_h = 135
    button_1 = pygame.Rect(button_x, button_1y, button_w, button_h)
    button_2 = pygame.Rect(button_x, button_2y, button_w, button_h)
    button_3 = pygame.Rect(button_x, button_3y, button_w, button_h)
    font = pygame.font.SysFont('Quicksand.ttf',200)
    font1 = pygame.font.SysFont('Quicksand.ttf', 100)
    font2 = pygame.font.SysFont('Quicksand.ttf', 60)
    ts = 60

elif display_siz == (2560,1440):
    screen = pygame.display.set_mode((2560,1440), pygame.FULLSCREEN)
    background_image = pygame.image.load(os.path.join('bj', "background2560X1440.png")).convert()
    main_image = pygame.image.load(os.path.join('MAINMENU', "MAINMENU2560X1440.png")).convert()
    button_1y = 557
    button_2y = 829
    button_3y = 1092
    button_x = 891
    button_w = 773
    button_h = 182
    button_1 = pygame.Rect(button_x, button_1y, button_w, button_h)
    button_2 = pygame.Rect(button_x, button_2y, button_w, button_h)
    button_3 = pygame.Rect(button_x, button_3y, button_w, button_h)
    font = pygame.font.SysFont('Quicksand.ttf', 300)
    font1 = pygame.font.SysFont('Quicksand.ttf', 150)
    font2 = pygame.font.SysFont('Quicksand.ttf', 90)
    ts = 90

elif display_siz == (3840,2160):
    screen = pygame.display.set_mode((3840,2160), pygame.FULLSCREEN)
    background_image = pygame.image.load(os.path.join('bj', "background3840X2160.png")).convert()
    main_image = pygame.image.load(os.path.join('MAINMENU', "MAINMENU3840X2160.png")).convert()
    button_1y = 836
    button_2y = 1244
    button_3y = 1638
    button_x = 1336
    button_w = 1159
    button_h = 272
    button_1 = pygame.Rect(button_x, button_1y, button_w, button_h)
    button_2 = pygame.Rect(button_x, button_2y, button_w, button_h)
    button_3 = pygame.Rect(button_x, button_3y, button_w, button_h)
    font = pygame.font.SysFont('Quicksand.ttf', 800)
    font1 = pygame.font.SysFont('Quicksand.ttf', 400)
    font2 = pygame.font.SysFont('Quicksand.ttf', 240)
    ts = 240

else:
    screen = pygame.display.set_mode((1366, 768), pygame.RESIZABLE)
    background_image = pygame.image.load(os.path.join('bj', "background1366X768.png")).convert()
    main_image = pygame.image.load(os.path.join('MAINMENU', "MAINMENU1366X768.png")).convert()
    button_1y = 298
    button_2y = 445
    button_3y = 585
    button_x = 490
    button_w = 380
    button_h = 95
    button_1 = pygame.Rect(button_x, button_1y, button_w, button_h)
    button_2 = pygame.Rect(button_x, button_2y, button_w, button_h)
    button_3 = pygame.Rect(button_x, button_3y, button_w, button_h)
    font = pygame.font.Font('Quicksand.ttf', 100)
    font1 = pygame.font.SysFont('Quicksand.ttf', 50)
    font2 = pygame.font.SysFont('Quicksand.ttf', 30)
    ts = 30



def main_menu():
    while True:

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



        screen.blit(main_image, [0, 0])


        mx, my = pygame.mouse.get_pos()


        if button_1.collidepoint((mx, my)) and click:
            clicksound.play()
            game()
        if button_2.collidepoint((mx, my)) and click:
            clicksound.play()
            store()
        if button_3.collidepoint((mx,my)) and click:
            clicksound.play()
            pygame.quit()
            sys.exit()




        

        pygame.display.update()

        mainClock.tick(60)






#game code
def game():
    running = True
    while running:
        screen.blit(background_image, [0, 0])


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
                    running = False



            print(display_siz)

        pygame.display.update()

#game pause code
def pause():
    running = True
    while running:
        screen.fill((74, 224, 191))

        def draw_text(text, font, color, surface, x,y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.center = (x,y)
            surface.blit(textobj, textrect)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        if button_1.collidepoint((mx, my)) and click:
            game()
        if button_2.collidepoint((mx, my)) and click:
           running = False
           running = False
        if button_3.collidepoint((mx, my)) and click:
            pygame.quit()
            sys.exit()

        pygame.draw.rect(screen, (255, 255, 244), button_1)
        pygame.draw.rect(screen, (255, 255, 244), button_2)
        pygame.draw.rect(screen, (255, 50, 50), button_3)

        draw_text('CONTINUE', font1, (0, 0, 0), screen, button_x+(button_w/2), button_1y+(button_h/2))
        draw_text('MAIN MENU', font1, (0, 0, 0), screen, button_x+(button_w/2), button_2y+(button_h/2))
        draw_text('QUIT', font1, (255,255,255), screen, button_x+(button_w/2), button_3y+(button_h/2))
        draw_text('PAUSED', font, (0, 0, 0), screen, button_x + (button_w / 2), (button_3y + (button_h / 2))/4)

        pygame.display.update()
        mainClock.tick(60)

#game over code
def gameover():
    running = True
    while running:
        screen.fill((0, 0, 0))

        def draw_text(text, font, color, surface, x,y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.center = (x,y)
            surface.blit(textobj, textrect)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        if button_1.collidepoint((mx, my)) and click:
            game()
        if button_2.collidepoint((mx, my)) and click:
           running = False
           running = False
        if button_3.collidepoint((mx, my)) and click:
            pygame.quit()
            sys.exit()

        pygame.draw.rect(screen, (255, 255, 244), button_1)
        pygame.draw.rect(screen, (255, 255, 244), button_2)
        pygame.draw.rect(screen, (255, 50, 50), button_3)

        draw_text('START AGAIN', font1, (0, 0, 0), screen, button_x+(button_w/2), button_1y+(button_h/2))
        draw_text('MAIN MENU', font1, (0, 0, 0), screen, button_x+(button_w/2), button_2y+(button_h/2))
        draw_text('QUIT', font1, (255,255,255), screen, button_x+(button_w/2), button_3y+(button_h/2))
        draw_text('GAME OVER', font, (255, 24, 24), screen, button_x + (button_w / 2), (button_3y + (button_h / 2))/4)

        pygame.display.update()
        mainClock.tick(60)

#store
def store():
    p = 1
    running = True
    while running:
        storeBG = pygame.image.load(os.path.join("Store","BG.png")).convert()
        screen.blit(pygame.transform.scale(storeBG, display_siz), [0, 0])
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        BSX = 100
        BSY = 50
        BG_B = pygame.Rect(250, 150, BSX, BSY)
        P_B = pygame.Rect(400, 150, BSX, BSY)

        pygame.draw.rect(screen, (255, 255, 244), BG_B)
        pygame.draw.rect(screen, (255, 255, 200), P_B)

        mx, my = pygame.mouse.get_pos()

        if BG_B.collidepoint((mx, my)) and click:
            p=1
        if P_B.collidepoint((mx, my)) and click:
            p=2

        
        
        def draw_text(text, font, color, surface, x,y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.center = (x,y)
            surface.blit(textobj, textrect)
        
        
        def store_BG(): #background
            ISX = 576
            ISY = 324
            BG1 = pygame.image.load(os.path.join("Store","1.png"))
            BG2 = pygame.image.load(os.path.join("Store","2.png"))
            BG3 = pygame.image.load(os.path.join("Store","3.png"))
            BG4 = pygame.image.load(os.path.join("Store","4.png"))

            screen.blit(pygame.transform.scale(BG1, (ISX,ISY)), [300, 250])
            screen.blit(pygame.transform.scale(BG2, (ISX,ISY)), [1100, 250])
            screen.blit(pygame.transform.scale(BG3, (ISX,ISY)), [300, 700])
            screen.blit(pygame.transform.scale(BG4, (ISX,ISY)), [1100, 700])

            draw_text('Select', font2, (255, 255, 255), screen, 300+(ISX/2), 250+ISY+30)
            draw_text('Select', font2, (255, 255, 255), screen, 1100+(ISX/2), 250+ISY+30)
            draw_text('Select', font2, (255, 255, 255), screen, 300+(ISX/2), 700+ISY+30)
            draw_text('Select', font2, (255, 255, 255), screen, 1100+(ISX/2), 700+ISY+30)

        def store_P(): #player
            ISX = 576
            ISY = 324
            BG1 = pygame.image.load(os.path.join("Store","p1.png"))
            BG2 = pygame.image.load(os.path.join("Store","p2.png"))
            BG3 = pygame.image.load(os.path.join("Store","p3.png"))
            BG4 = pygame.image.load(os.path.join("Store","p4.png"))

            screen.blit(pygame.transform.scale(BG1, (ISX,ISY)), [300, 250])
            screen.blit(pygame.transform.scale(BG2, (ISX,ISY)), [1100, 250])
            screen.blit(pygame.transform.scale(BG3, (ISX,ISY)), [300, 700])
            screen.blit(pygame.transform.scale(BG4, (ISX,ISY)), [1100, 700])

            draw_text('Select', font2, (255, 255, 255), screen, 300+(ISX/2), 250+ISY+30)
            draw_text('Select', font2, (255, 255, 255), screen, 1100+(ISX/2), 250+ISY+30)
            draw_text('Select', font2, (255, 255, 255), screen, 300+(ISX/2), 700+ISY+30)
            draw_text('Select', font2, (255, 255, 255), screen, 1100+(ISX/2), 700+ISY+30)

        if p == 1:
            store_BG()
        elif p == 2:
            store_P()
        else:
            p = 1

        #screen.fill((0, 0, 0)) 
   


        draw_text('STORE', font1, (255, 255, 255), screen, wi /2, ts)
        #draw_text('//', font2, (255, 255, 255), screen, wi/2 , ts * 2.5)
        #raw_text(' //', font2, (255, 255, 255), screen, wi / 2, ts * 4)

        

        
        
            
        pygame.display.update()
        mainClock.tick(60)



main_menu()
