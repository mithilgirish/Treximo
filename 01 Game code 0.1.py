import pygame,sys
import os
from pygame.locals import *

mainClock = pygame.time.Clock() #FPS
pygame.init() 
 
pygame.display.set_caption("CS project") #name

programIcon = pygame.image.load('logo_jankesRun_C.png')
pygame.display.set_icon(programIcon)# logo/icon
 
display_siz = (pygame.display.Info().current_w, pygame.display.Info().current_h)#display size
wi = pygame.display.Info().current_w
he = pygame.display.Info().current_h


clicksound = pygame.mixer.Sound(os.path.join("SFX","click.ogg"))#click sound


screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) #initialize
main_image = pygame.image.load(os.path.join('MAINMENU', "MAINMENU3840X2160.png")).convert()


background_image = pygame.image.load(os.path.join("Background","1.png"))
#background_image = pygame.image.load(os.path.join("Background","2.png"))
#background_image = pygame.image.load(os.path.join("Background","3.png"))
#background_image = pygame.image.load(os.path.join("Background","4.png"))

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





 
if display_siz == (1366,768):
    screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
    background_image = pygame.transform.scale(background_image, display_siz)
    main_image = pygame.transform.scale(main_image, display_siz)
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
    
elif display_siz == (1920,1080):
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    background_image = pygame.transform.scale(background_image, display_siz)
    main_image = pygame.transform.scale(main_image, display_siz)
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
    background_image = pygame.transform.scale(background_image, display_siz)
    main_image = pygame.transform.scale(main_image, display_siz)
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
    background_image = pygame.transform.scale(background_image, display_siz)
    main_image = pygame.transform.scale(main_image, display_siz)
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
    display_siz = (1366, 768)
    background_image = pygame.transform.scale(background_image, display_siz)
    main_image = pygame.transform.scale(main_image, display_siz), [0, 0]
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
    #background
    width = 1920
    i = 0
    #player 
    n=0
    x = width/2
    y = 650
    vel_x = 10
    vel_y = 10
    jump = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #screen.fill((0,0,0))

        #Create looping background
        screen.blit(background_image, (i, 0))
        screen.blit(background_image, (width+i, 0))
        if i == -width:
            screen.blit(background_image, (width+i, 0))
            i = 0
        i -= 12

        
        #player
        
        screen.blit(player1[n],(int(x),int(y))) #player1
        #screen.blit(player2[n],(int(x),int(y))) #player2
        #screen.blit(player3[n],(int(x),int(y))) #player3
        #screen.blit(player4[n],(int(x),int(y))) #player4
        
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

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
                    running = False

            
        pygame.time.Clock().tick(60)
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
        screen.blit(pygame.transform.scale(storeBG, display_siz), [0, 0])#backgrond

        back_b = pygame.image.load(os.path.join("Store","back.png"))
        screen.blit(pygame.transform.scale(back_b, (80,80)), [10, 10])#back button
        
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
        B_B = pygame.Rect(10,10, 80,80)

        pygame.draw.rect(screen, (255, 255, 244), BG_B)
        pygame.draw.rect(screen, (255, 255, 200), P_B)

        mx, my = pygame.mouse.get_pos()

        if BG_B.collidepoint((mx, my)) and click:
            p=1
        if P_B.collidepoint((mx, my)) and click:
            p=2
        if B_B.collidepoint((mx, my)) and click:
            running = False
            
        
        #pygame.draw.rect(screen, (255, 255, 200), B_B)
        
        
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

