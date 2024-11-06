import pygame
import sys
from  card import Card
def run():


    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Дурак1")
    bg_color = "green"
    card = Card()
    player = card.razdacha()
    nachal = False
    nachalvod = False
    atack=True
    pobito=False
    otvet = True
    hod2 = True
    screen.fill(bg_color)
    while True:

        card.add(screen, player)

        pygame.display.flip()
        if nachal:
            nach=card.prinis(screen, bg_color, player)
            if nach:
                nachal=False
                nachalvod=False
            else:
                nachal = False
                nachalvod = True

        if atack == True and hod2 == False:
            karta = card.prini(screen)
            atack=False

        if pobito == True:
            boas = card.bitoan(player)
            if boas==True:
                screen.fill(bg_color)
                pobito = False
                otvet = True
                atack = True
                hod2 = True



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if nachalvod==False and hod2==True:
                        screen.fill(bg_color)
                        card.hod(screen, player, 0)
                        nachal= True
                    if atack == False and otvet == True and hod2 == False:
                        prov = card.otvet(screen, karta, player, 0, bg_color)
                        if prov == True:
                            pobito = True
                            otvet = False
                if event.key == pygame.K_2:
                    if nachalvod == False and hod2==True:
                        screen.fill(bg_color)
                        card.hod(screen, player, 1)
                        nachal = True
                    if atack == False and otvet == True and hod2 == False:
                        prov = card.otvet(screen, karta, player, 1, bg_color)
                        if prov == True:
                            pobito = True
                            otvet = False
                if event.key == pygame.K_3:
                    if nachalvod == False and hod2==True:
                        screen.fill(bg_color)
                        card.hod(screen, player, 2)
                        nachal= True
                    if atack == False and otvet==True and hod2==False:
                        prov=card.otvet(screen, karta, player, 2, bg_color)
                        if prov==True:
                            pobito=True
                            otvet = False
                if event.key == pygame.K_4:
                    if nachalvod == False and hod2==True:
                        screen.fill(bg_color)
                        card.hod(screen, player, 3)
                        nachal= True
                    if atack == False and otvet==True and hod2==False:
                        prov=card.otvet(screen, karta, player, 3, bg_color)
                        if prov==True:
                            pobito=True
                            otvet = False
                if event.key == pygame.K_5:
                    if nachalvod == False and hod2==True:
                        screen.fill(bg_color)
                        card.hod(screen, player, 4)
                        nachal= True
                    if atack == False and otvet==True and hod2==False:
                        prov=card.otvet(screen, karta, player, 4, bg_color)
                        if prov==True:
                            pobito=True
                            otvet = False
                if event.key == pygame.K_6:
                    if nachalvod == False and hod2==True:
                        screen.fill(bg_color)
                        card.hod(screen, player, 5)
                        nachal= True
                    if atack == False and otvet==True and hod2==False:
                        prov=card.otvet(screen, karta, player, 5, bg_color)
                        if prov==True:
                            pobito=True
                            otvet = False
                if event.key == pygame.K_9:
                    if atack == False and otvet==True and hod2==False:
                        card.beru(screen,karta, player, bg_color)
                        atack = True
                if event.key == pygame.K_0:
                    if nachalvod:
                        screen.fill(bg_color)
                        card.bito(player)
                        nachalvod = False
                        hod2 = False


run()