import pygame
import sys 
import os
import random
from pygame.locals import *

mainClock = pygame.time.Clock() #FPS
pygame.init() 
 
pygame.display.set_caption("Treximo") #name

programIcon = pygame.image.load('LOGO.png')
pygame.display.set_icon(programIcon)# logo/icon
 
display_siz = (pygame.display.Info().current_w, pygame.display.Info().current_h)#display size


clicksound = pygame.mixer.Sound(os.path.join("SFX","click.ogg"))#click sound


screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) #initialize

#DATA
player_data = {"p1":["yes"],"p2":["yes","no"],"p3":["yes","no"],"p4":["yes","no"]}
BG_data = {"b1":["yes"],"b2":["yes","no"],"b3":["yes","no"],"b4":["yes","no"]}
coins = 0
high_score = 0


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




#correction factor
 
if display_siz == (1366,768):
    DS = 1
    screen = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)
    CF = 0.71
    
elif display_siz == (1920,1080):
    DS = 2
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    CF = 1
    

elif display_siz == (2560,1440):
    DS = 3
    screen = pygame.display.set_mode((2560,1440), pygame.FULLSCREEN)
    CF = 1.31
    

elif display_siz == (3840,2160):
    DS = 4
    screen = pygame.display.set_mode((3840,2160), pygame.FULLSCREEN)
    CF = 2
    

else:
    DS = 1
    screen = pygame.display.set_mode((1366, 768), pygame.RESIZABLE)
    display_siz = (1366, 768)
    CF = 0.71
   




#main menu
main_image = pygame.image.load(os.path.join("Background", "BG.png"))
main_image_mountain = pygame.image.load(os.path.join("Background", "Mountain.png"))
main_image_star1 = pygame.image.load(os.path.join("Background", "star 1.png"))
main_image_star2 = pygame.image.load(os.path.join("Background", "star 2.png"))

main_image = pygame.transform.scale(main_image, display_siz) 
main_image_mountain = pygame.transform.scale(main_image_mountain, display_siz)
main_image_star1 = pygame.transform.scale(main_image_star1, (30*CF,30*CF))
main_image_star2 = pygame.transform.scale(main_image_star2, (30*CF,30*CF))

button_1y = int(418*CF)
button_2y = int(622*CF)
button_3y = int(819*CF)
button_x = int(665*CF)

button_w = int(578*CF)
button_h = int(135*CF)

button_1 = pygame.Rect(button_x, button_1y, button_w, button_h)
button_2 = pygame.Rect(button_x, button_2y, button_w, button_h)
button_3 = pygame.Rect(button_x, button_3y, button_w, button_h)

font = pygame.font.Font('Quicksand.ttf',int(200*CF))
font1 = pygame.font.Font('Quicksand.ttf', int(100*CF))
font2 = pygame.font.Font('Quicksand.ttf', int(60*CF))
font3 = pygame.font.Font('Quicksand.ttf', int(30*CF))
font4 = pygame.font.Font('Quicksand.ttf', int(45*CF))
font4_s = pygame.font.Font('Quicksand.ttf', int(46*CF))


def load():
    LOAD_f = pygame.font.Font('FFF.ttf',int(180*CF))
    
    for i in range(0,256):
        pygame.draw.rect(screen, (i, i, i), (pygame.Rect((display_siz[0]-(300*CF))/2, 800*CF, 300*CF, 10*CF)))
        pygame.draw.rect(screen, (i, i, i), (pygame.Rect((display_siz[0]-(300*CF))/2, 750*CF, 300*CF, 10*CF)))
        pygame.draw.rect(screen, (i, i, i), (pygame.Rect((display_siz[0]+(290*CF))/2, 750*CF, 10*CF, 60*CF)))
        pygame.draw.rect(screen, (i, i, i), (pygame.Rect((display_siz[0]-(290*CF))/2, 750*CF, 10*CF, 50*CF)))

        def draw_text(text, font, color, surface, x,y):
                    textobj = font.render(text, 1, color)
                    textrect = textobj.get_rect()
                    textrect.center = (x,y)
                    surface.blit(textobj, textrect)
                    
        draw_text('TREXIMO', LOAD_f, (i, i, i), screen, display_siz[0]/2, 300*CF)
        pygame.draw.rect(screen, (i, i, i), (pygame.Rect((display_siz[0]-(300*CF))/2, 750*CF, (i/6)*CF, 50*CF)))


        pygame.display.update()
    i = 256
    while i != 1800:
        pygame.draw.rect(screen, (255, 255, 255), (pygame.Rect((display_siz[0]-(300*CF))/2, 800*CF, 300*CF, 10*CF)))
        pygame.draw.rect(screen, (255, 255, 255), (pygame.Rect((display_siz[0]-(300*CF))/2, 750*CF, 300*CF, 10*CF)))
        pygame.draw.rect(screen, (255, 255, 255), (pygame.Rect((display_siz[0]+(290*CF))/2, 750*CF, 10*CF, 60*CF)))
        pygame.draw.rect(screen, (255, 255, 255), (pygame.Rect((display_siz[0]-(290*CF))/2, 750*CF, 10*CF, 50*CF)))

        pygame.draw.rect(screen, (255, 255, 255), (pygame.Rect((display_siz[0]-(300*CF))/2, 750*CF, (i/6)*CF, 50*CF)))

        i = i+1
        pygame.display.update()
    if i == 1800:
        main_menu()
    
    
def main_menu():
    menu_song = pygame.mixer.music.load(os.path.join("BG songs","Main menu.mp3"))
    pygame.mixer.music.play(-1)
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
        #stars
        screen.blit(main_image_star1, [random.randint(0,display_siz[0]), random.randint(0,display_siz[1]-400*CF)])
        screen.blit(main_image_star1, [random.randint(0,display_siz[0]), random.randint(0,display_siz[1]-400*CF)])
        screen.blit(main_image_star2, [random.randint(0,display_siz[0]), random.randint(0,display_siz[1]-400*CF)])
        screen.blit(main_image_star2, [random.randint(0,display_siz[0]), random.randint(0,display_siz[1]-400*CF)])
        #layer
        screen.blit(main_image_mountain, [0, 0])
        

        mx, my = pygame.mouse.get_pos()


        if button_1.collidepoint((mx, my)) and click:
            clicksound.play()
            game()
            pygame.mixer.music.stop()
        if button_2.collidepoint((mx, my)) and click:
            clicksound.play()
            mainClock.tick(60)
            store()
        if button_3.collidepoint((mx,my)) and click:
            clicksound.play()
            pygame.quit()
            sys.exit()


        pygame.display.update()
        mainClock.tick(3*CF)

def buy(buy_image,s_name,BorP, AV = 0):
    font_n = pygame.font.Font('Quicksand.ttf',int(115*CF))
    font_n2 = pygame.font.Font('Quicksand.ttf',int(116*CF))
    running = True
    
    
    while running:
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
                    
        yes = pygame.Rect(710*CF, 850*CF, 225*CF, 85*CF)
        no = pygame.Rect(980*CF, 850*CF, 225*CF, 85*CF)
        ok = pygame.Rect(830*CF, 840*CF, 260*CF, 100*CF)
        
        
        base_store = pygame.image.load(os.path.join("Store","base_store.png"))
        buy_button_1 = pygame.image.load(os.path.join("Store","buy button_1.png"))
        buy_button_2 = pygame.image.load(os.path.join("Store","buy button_2.png"))
        select_button = pygame.image.load(os.path.join("Store","select button.png"))
        
        screen.blit(pygame.transform.scale(base_store, (755*CF,960*CF)), [display_siz[0]/2-((755*CF)/2), 50*CF])

        def draw_text(text, font, color, surface, x,y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.center = (x,y)
            surface.blit(textobj, textrect)

        #NAME
        draw_text(s_name, font_n, (0,0,0), screen, (display_siz[0]/2)+3, int(680*CF)+3)#shadow layer
        draw_text(s_name, font_n2, (0,0,0), screen, (display_siz[0]/2), int(680*CF))#outline layer
        draw_text(s_name, font_n, (255, 255, 255), screen, (display_siz[0]/2)-2, int(680*CF)-2)
        
        mx, my = pygame.mouse.get_pos()

        if AV == 0:
            
                   
            screen.blit(pygame.transform.scale(select_button, (755*CF,960*CF)), [display_siz[0]/2-((755*CF)/2), 50*CF])

            if yes.collidepoint((mx, my)) and click:
                if BorP[0] == "p":
                    player_data["p1"][0] = "no"
                    player_data["p2"][1] = "no"
                    player_data["p3"][1] = "no"
                    player_data["p4"][1] = "no"
                    if BorP[1] == "1":
                        player_data[BorP][0] = "yes"
                    else:
                        player_data[BorP][1] = "yes"
                if BorP[0] == "b":
                    BG_data["b1"][0] = "no"
                    BG_data["b2"][1] = "no"
                    BG_data["b3"][1] = "no"
                    BG_data["b4"][1] = "no"
                    if BorP[1] == "1":
                        BG_data[BorP][0] = "yes"
                    else:
                        BG_data[BorP][1] = "yes"
                running = False
                    
            if no.collidepoint((mx, my)) and click:
                running = False
                
        if AV == 1: #yes or no
            screen.blit(pygame.transform.scale(buy_button_1, (755*CF,960*CF)), [display_siz[0]/2-((755*CF)/2), 50*CF])

            if yes.collidepoint((mx, my)) and click:
                i = 0
                AV = 2
            if no.collidepoint((mx, my)) and click:
                running = False
            
                
        if AV == 2: #okay button
            screen.blit(pygame.transform.scale(buy_button_2, (755*CF,960*CF)), [display_siz[0]/2-((755*CF)/2), 50*CF])
            
            if i != 5:
                i = i+1
            if i == 5:
                if ok.collidepoint((mx, my)) and click:
                    running = False

        screen.blit(pygame.transform.scale(buy_image, (ISX,ISY)), [display_siz[0]/2-((ISX)/2), 300*CF])

        
        
        pygame.display.update()
        mainClock.tick(60)
        
#store
def store():
    p = 1 #page
    running = True
    while running:
        
        global ISX,ISY
        storeBG = pygame.image.load(os.path.join("Store","BG.png")).convert()
        screen.blit(pygame.transform.scale(storeBG, display_siz), [0, 0])#backgrond

        def draw_text(text, font, color, surface, x,y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.center = (x,y)
            surface.blit(textobj, textrect)

        draw_text('STORE', font1, (255, 255, 255), screen, display_siz[0]/2, int(60*CF))

        button = pygame.image.load(os.path.join("Store","button.png"))#button
        button_ = pygame.image.load(os.path.join("Store","button_.png"))

        #coins
        draw_text("Coins: "+str(coins), font4, (255, 255, 255), screen, display_siz[0]-int(130*CF) ,30*CF)


        storeBG_L1 = pygame.image.load(os.path.join("Store","BG_layer1.png"))
        screen.blit(pygame.transform.scale(storeBG_L1, (1430*CF,850*CF)), [270*CF, 220*CF])

        back_b = pygame.image.load(os.path.join("Store","back.png"))
        screen.blit(pygame.transform.scale(back_b, (80*CF,80*CF)), [10*CF, 10*CF])#back button
        
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
        #button size
        BSX = int(180*CF)
        BSY = int(70*CF)
        BG_B = pygame.Rect(320*CF, 150*CF, BSX, BSY) #BG
        P_B = pygame.Rect(520*CF, 150*CF, BSX-(50*CF), BSY) #Player
        
        B_B = pygame.Rect(10*CF,10*CF, 80*CF,80*CF) #back button 

        
        #box size
        ISX = 576*CF
        ISY = 324*CF
        

        #coins
        BSW = int(180*CF)
        BSH = int(60*CF)
        BUY1 = pygame.Rect(300*CF+(ISX/2)-(BSW/2), 275*CF+ISY-(BSH/2), BSW, BSH)
        BUY2 = pygame.Rect(1100*CF+(ISX/2)-(BSW/2), 275*CF+ISY-(BSH/2), BSW, BSH)
        BUY3 = pygame.Rect(300*CF+(ISX/2)-(BSW/2), 695*CF+ISY-(BSH/2), BSW, BSH)
        BUY4 = pygame.Rect(1100*CF+(ISX/2)-(BSW/2), 695*CF+ISY-(BSH/2), BSW, BSH)
        coin = pygame.image.load(os.path.join("Store","coin.png"))

        BSW2 = int(200*CF)
        BSH2 = int(60*CF)


        mx, my = pygame.mouse.get_pos()

        if BG_B.collidepoint((mx, my)) and click:
            p=1
        if P_B.collidepoint((mx, my)) and click:
            p=2
        if B_B.collidepoint((mx, my)) and click:
            running = False
            


        
        def store_BG(): #background
            pygame.draw.rect(screen, (226, 226, 233), BG_B)
            pygame.draw.rect(screen, (22, 22, 29), P_B)

            draw_text('Background', font3, (0, 0, 0), screen, 320*CF+(BSX/2), 150*CF+(BSY/2))
            draw_text('Player', font3, (255, 255, 255), screen, 520*CF+((BSX-(50*CF))/2), 150*CF+(BSY/2))

            BG1 = pygame.image.load(os.path.join("Store","1.png"))
            BG2 = pygame.image.load(os.path.join("Store","2.png"))
            BG3 = pygame.image.load(os.path.join("Store","3.png"))
            BG4 = pygame.image.load(os.path.join("Store","4.png"))

            screen.blit(pygame.transform.scale(BG1, (ISX,ISY)), [300*CF, 245*CF])
            screen.blit(pygame.transform.scale(BG2, (ISX,ISY)), [1100*CF, 245*CF])
            screen.blit(pygame.transform.scale(BG3, (ISX,ISY)), [300*CF, 665*CF])
            screen.blit(pygame.transform.scale(BG4, (ISX,ISY)), [1100*CF, 665*CF])
            
            

            if BG_data["b1"][0] == "yes":
                draw_text('Selected', font2, (255, 255, 255), screen, 300*CF+(ISX/2), 275*CF+ISY)
            if BG_data["b2"][1] == "yes":
                draw_text('Selected', font2, (255, 255, 255), screen, 1100*CF+(ISX/2), 275*CF+ISY)
            if BG_data["b3"][1] == "yes":
                draw_text('Selected', font2, (255, 255, 255), screen, 300*CF+(ISX/2), 695*CF+ISY)
            if BG_data["b4"][1] == "yes":
                draw_text('Selected', font2, (255, 255, 255), screen, 1100*CF+(ISX/2), 695*CF+ISY)

            #buy with coins button
            CS = 50*CF

            if BG_data["b2"][0] == "no":
                screen.blit(pygame.transform.scale(button, (BSW, BSH)), [1100*CF+(ISX/2)-(BSW/2), 275*CF+ISY-(BSH/2)])
                draw_text('500', font2, (0, 0, 0), screen, 1100*CF+(ISX/2)+(CS/2), 275*CF+ISY)
                screen.blit(pygame.transform.scale(coin, (CS,CS)), [1100*CF+(ISX/2)-CS-(35*CF), 275*CF+ISY-(CS/2)])

            if BG_data["b3"][0] == "no":
                screen.blit(pygame.transform.scale(button, (BSW, BSH)), [300*CF+(ISX/2)-(BSW/2), 695*CF+ISY-(BSH/2)])
                draw_text('500', font2, (0, 0, 0), screen, 300*CF+(ISX/2)+(CS/2), 695*CF+ISY)
                screen.blit(pygame.transform.scale(coin, (CS,CS)), [300*CF+(ISX/2)-CS-(35*CF), 695*CF+ISY-(CS/2)])

            if BG_data["b4"][0] == "no":
                screen.blit(pygame.transform.scale(button, (BSW, BSH)), [1100*CF+(ISX/2)-(BSW/2), 695*CF+ISY-(BSH/2)])
                draw_text('500', font2, (0, 0, 0), screen, 1100*CF+(ISX/2)+(CS/2), 695*CF+ISY)
                screen.blit(pygame.transform.scale(coin, (CS,CS)), [1100*CF+(ISX/2)-CS-(35*CF), 695*CF+ISY-(CS/2)])

            if BUY2.collidepoint((mx, my)) and click and BG_data["b2"][0] == "no":
                buy(BG2,"MIRAMAR","b2",1)
                    
            if BUY3.collidepoint((mx, my)) and click and BG_data["b3"][0] == "no":
                buy(BG3,"ERANGEL","b3",1)
                    
            if BUY4.collidepoint((mx, my)) and click and BG_data["b4"][0] == "no":
                buy(BG4,"SANHOK","b4",1)

            #select
            if BG_data["b1"][0] == "no":
                screen.blit(pygame.transform.scale(button_, (BSW2, BSH2)), [300*CF+(ISX/2)-(BSW2/2), 275*CF+ISY-(BSH/2)])
                draw_text('Select', font2, (255, 255, 255), screen, 300*CF+(ISX/2), 275*CF+ISY)
                

            if BG_data["b2"][1] == "no":
                screen.blit(pygame.transform.scale(button_, (BSW2, BSH2)), [1100*CF+(ISX/2)-(BSW2/2), 275*CF+ISY-(BSH/2)])
                draw_text('Select', font2, (255, 255, 255), screen, 1100*CF+(ISX/2), 275*CF+ISY)
                
                    
            if BG_data["b3"][1] == "no":        
                screen.blit(pygame.transform.scale(button_, (BSW2, BSH2)), [300*CF+(ISX/2)-(BSW2/2), 695*CF+ISY-(BSH/2)])
                draw_text('Select', font2, (255, 255, 255), screen, 300*CF+(ISX/2), 695*CF+ISY)
                
                    
            if BG_data["b4"][1] == "no": 
                screen.blit(pygame.transform.scale(button_, (BSW2, BSH2)), [1100*CF+(ISX/2)-(BSW2/2), 695*CF+ISY-(BSH/2)])
                draw_text('Select', font2, (255, 255, 255), screen, 1100*CF+(ISX/2), 695*CF+ISY)


            if BUY1.collidepoint((mx, my)) and click and BG_data["b1"][0] == "no":
                buy(BG1,"VIKENDI","b1",0)
                
            if BUY2.collidepoint((mx, my)) and click and BG_data["b2"][1] == "no" and BG_data["b2"][0] == "yes":
                buy(BG2,"MIRAMAR","b2",0)
                    
            if BUY3.collidepoint((mx, my)) and click and BG_data["b3"][1] == "no" and BG_data["b3"][0] == "yes":
                buy(BG3,"ERANGEL","b3",0)
                    
            if BUY4.collidepoint((mx, my)) and click and BG_data["b4"][1] == "no" and BG_data["b4"][0] == "yes":
                buy(BG4,"SANHOK","b4",0)
                
            

            
        def store_P(): #player
            pygame.draw.rect(screen, (22, 22, 29), BG_B)
            pygame.draw.rect(screen, (226, 226, 233), P_B)

            draw_text('Background', font3, (255, 255, 255), screen, 320*CF+(BSX/2), 150*CF+(BSY/2))
            draw_text('Player', font3, (0, 0, 0), screen, 520*CF+((BSX-(50*CF))/2), 150*CF+(BSY/2))
            
            BG1 = pygame.image.load(os.path.join("Store","p1.png"))
            BG2 = pygame.image.load(os.path.join("Store","p2.png"))
            BG3 = pygame.image.load(os.path.join("Store","p3.png"))
            BG4 = pygame.image.load(os.path.join("Store","p4.png"))

            screen.blit(pygame.transform.scale(BG1, (ISX,ISY)), [300*CF, 245*CF])
            screen.blit(pygame.transform.scale(BG2, (ISX,ISY)), [1100*CF, 245*CF])
            screen.blit(pygame.transform.scale(BG3, (ISX,ISY)), [300*CF, 665*CF])
            screen.blit(pygame.transform.scale(BG4, (ISX,ISY)), [1100*CF, 665*CF])

            if player_data["p1"][0] == "yes":
                draw_text('Selected', font2, (255, 255, 255), screen, 300*CF+(ISX/2), 275*CF+ISY)
            if player_data["p2"][1] == "yes":
                draw_text('Selected', font2, (255, 255, 255), screen, 1100*CF+(ISX/2), 275*CF+ISY)
            if player_data["p3"][1] == "yes":
                draw_text('Selected', font2, (255, 255, 255), screen, 300*CF+(ISX/2), 695*CF+ISY)
            if player_data["p4"][1] == "yes":
                draw_text('Selected', font2, (255, 255, 255), screen, 1100*CF+(ISX/2), 695*CF+ISY)

            #buy with coins button

            CS = 50*CF

            if player_data["p2"][0] == "no":
                screen.blit(pygame.transform.scale(button, (BSW, BSH)), [1100*CF+(ISX/2)-(BSW/2), 275*CF+ISY-(BSH/2)])
                draw_text('500', font2, (0, 0, 0), screen, 1100*CF+(ISX/2)+(CS/2), 275*CF+ISY)
                screen.blit(pygame.transform.scale(coin, (CS,CS)), [1100*CF+(ISX/2)-CS-(35*CF), 275*CF+ISY-(CS/2)])

            if player_data["p3"][0] == "no":
                screen.blit(pygame.transform.scale(button, (BSW, BSH)), [300*CF+(ISX/2)-(BSW/2), 695*CF+ISY-(BSH/2)])
                draw_text('500', font2, (0, 0, 0), screen, 300*CF+(ISX/2)+(CS/2), 695*CF+ISY)
                screen.blit(pygame.transform.scale(coin, (CS,CS)), [300*CF+(ISX/2)-CS-(35*CF), 695*CF+ISY-(CS/2)])

            if player_data["p4"][0] == "no":
                screen.blit(pygame.transform.scale(button, (BSW, BSH)), [1100*CF+(ISX/2)-(BSW/2), 695*CF+ISY-(BSH/2)])
                draw_text('500', font2, (0, 0, 0), screen, 1100*CF+(ISX/2)+(CS/2), 695*CF+ISY)
                screen.blit(pygame.transform.scale(coin, (CS,CS)), [1100*CF+(ISX/2)-CS-(35*CF), 695*CF+ISY-(CS/2)])


            if BUY2.collidepoint((mx, my)) and click and player_data["p2"][0] == "no":
                buy(BG2,"ADONIA","p2",1)
                    
            if BUY3.collidepoint((mx, my)) and click and player_data["p3"][0] == "no":
                buy(BG3,"REKO","p3",1)
                    
            if BUY4.collidepoint((mx, my)) and click and player_data["p4"][0] == "no":
                buy(BG4,"MELANIE","p3",1)
                
            #select
            if player_data["p1"][0] == "no":
                screen.blit(pygame.transform.scale(button_, (BSW2, BSH2)), [300*CF+(ISX/2)-(BSW2/2), 275*CF+ISY-(BSH/2)])
                draw_text('Select', font2, (255, 255, 255), screen, 300*CF+(ISX/2), 275*CF+ISY)
                

            if player_data["p2"][1] == "no":
                screen.blit(pygame.transform.scale(button_, (BSW2, BSH2)), [1100*CF+(ISX/2)-(BSW2/2), 275*CF+ISY-(BSH/2)])
                draw_text('Select', font2, (255, 255, 255), screen, 1100*CF+(ISX/2), 275*CF+ISY)
                
                    
            if player_data["p3"][1] == "no":        
                screen.blit(pygame.transform.scale(button_, (BSW2, BSH2)), [300*CF+(ISX/2)-(BSW2/2), 695*CF+ISY-(BSH/2)])
                draw_text('Select', font2, (255, 255, 255), screen, 300*CF+(ISX/2), 695*CF+ISY)
                
                    
            if player_data["p4"][1] == "no": 
                screen.blit(pygame.transform.scale(button_, (BSW2, BSH2)), [1100*CF+(ISX/2)-(BSW2/2), 695*CF+ISY-(BSH/2)])
                draw_text('Select', font2, (255, 255, 255), screen, 1100*CF+(ISX/2), 695*CF+ISY)
                
            
                
            if BUY1.collidepoint((mx, my)) and click and player_data["p1"][0] == "no":
                    buy(BG1,"DRACO","p1",0)

            if BUY2.collidepoint((mx, my)) and click and player_data["p2"][1] == "no" and player_data["p2"][0] == "yes":
                    buy(BG2,"ADONIA","p2",0)

            if BUY3.collidepoint((mx, my)) and click and player_data["p3"][1] == "no" and player_data["p3"][0] == "yes":
                    buy(BG3,"REKO","p3",0)
                        
            if BUY4.collidepoint((mx, my)) and click and player_data["p3"][1] == "no" and player_data["p4"][0] == "yes":
                    buy(BG4,"MELANIE","p4",0)
            
                
            
            

        if p == 1:
            store_BG()
        elif p == 2:
            store_P()
        else:
            p = 1

   
        
  
        pygame.display.update()
        mainClock.tick(60)




#game code
def game():
    
    #game background and sound
    if BG_data["b1"][0] == "yes":
        background_image = pygame.image.load(os.path.join("Background","1.png"))
        BG_S_1 = pygame.mixer.music.load(os.path.join("BG songs","Main menu.mp3"))

    if BG_data["b2"][1] == "yes":
        background_image = pygame.image.load(os.path.join("Background","2.png"))
        BG_S_2 = pygame.mixer.music.load(os.path.join("BG songs","Main menu.mp3"))

    if BG_data["b3"][1] == "yes":
        background_image = pygame.image.load(os.path.join("Background","3.png"))
        BG_S_3 = pygame.mixer.music.load(os.path.join("BG songs","Main menu.mp3"))

    if BG_data["b4"][1] == "yes":
        background_image = pygame.image.load(os.path.join("Background","4.png"))
        BG_S_4 = pygame.mixer.music.load(os.path.join("BG songs","Main menu.mp3"))

    background_image = pygame.transform.scale(background_image, display_siz)
    pygame.mixer.music.play(-1)
    
    #background
    width = display_siz[0]
    i = 0
    
    #player
    n = 0
    PIX = (270*CF,359*CF) #size
    x = display_siz[0]/2
    y = display_siz[1]-(PIX[1])-170*CF
    vel_y = 10*CF #speed
    jump = False
    JN = 4 #jump height

    #score
    H_Score = 0
    DIS_I = 0.3*CF
    global high_score
    print(high_score)
    m = 0
    temp_coins = 0
    
    running_G = True
    while running_G:
        
        def draw_text(text, font, color, surface, x,y):
                    textobj = font.render(text, 1, color)
                    textrect = textobj.get_rect()
                    textrect.center = (x,y)
                    surface.blit(textobj, textrect)
        
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_G = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        #Create looping background
        screen.blit(background_image, (i, 0))
        screen.blit(background_image, (width+i, 0))
        if i <= -width:
            screen.blit(background_image, (width+i, 0))
            i = 0
        i -= abs(int(12*CF))



        #player
        if player_data["p1"][0] == "yes":
            screen.blit(pygame.transform.scale(player1[n],(PIX[0],PIX[1])),(int(x),int(y)))#player1

        if player_data["p2"][1] == "yes":
            screen.blit(pygame.transform.scale(player2[n],(PIX[0],PIX[1])),(int(x),int(y))) #player2

        if player_data["p3"][1] == "yes":
            screen.blit(pygame.transform.scale(player3[n],(PIX[0],PIX[1])),(int(x),int(y))) #player3

        if player_data["p4"][1] == "yes":
            screen.blit(pygame.transform.scale(player4[n],(PIX[0],PIX[1])),(int(x),int(y))) #player4
        
        n = n+1
        if n>=6:
            n=0
        #Jump
        userInput = pygame.key.get_pressed()
        if jump is False and userInput[pygame.K_SPACE]:
            jump = True
        if jump is True:
            n=7
            y -= vel_y*JN*CF
            vel_y -= 1
            if vel_y < -10*CF:
                jump = False
                vel_y = 10*CF

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()

        #score
        
        H_Score = H_Score + DIS_I
        draw_text((str(int(H_Score))), font2, (0, 0, 0), screen, width-int(105*CF) ,40*CF)
        
        if high_score <= H_Score and (high_score >= 50 or H_Score >= 50):
            high_score = H_Score
            if m <= 50:
                draw_text("High Score", font2, (0, 0, 0), screen, width/2 ,100*CF)
                m = m+1

        #coins
        draw_text("Coins:"+str(temp_coins), font4, (51, 0, 0), screen, width-int(125*CF) ,100*CF) 
        #pause
        P_B = pygame.Rect(10*CF,10*CF, 80*CF,80*CF)
        
        pause_b = pygame.image.load(os.path.join("Store","pause.png"))
        screen.blit(pygame.transform.scale(pause_b, (80*CF,80*CF)), [10*CF, 10*CF])#back button

        mx, my = pygame.mouse.get_pos()

        if P_B.collidepoint((mx, my)) and click:
            pause()
        
        #Refresh
        pygame.time.Clock().tick(60*CF)
        pygame.display.update()
        
        #game pause code
        def pause():
            nonlocal running_G
            running = True
            while running:
                screen.fill((74, 224, 191))

                

                click = False
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            mainClock.tick(60)
                            running = False
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                mx, my = pygame.mouse.get_pos()

                if button_1.collidepoint((mx, my)) and click:
                    mainClock.tick(60)
                    running = False
                if button_2.collidepoint((mx, my)) and click:
                    pygame.mixer.music.stop()
                    running = False
                    running_G = False                   
                    
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

                
                mainClock.tick(1)
                pygame.display.update()
    if running_G == False:
        main_menu()



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
            pygame.mixer.music.stop()
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



load()
