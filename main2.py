import pygame
import sys
from caRD import Card
def run():


    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Дурак")
    bg_color = "green"
    card = Card()
    player = card.razdacha()
    atack=True
    pobito=False
    otvet = True
    screen.fill(bg_color)
    while True:


        card.add(screen, player)
        pygame.display.flip()
        if atack:
            karta = card.prini(screen)
            atack=False

        if pobito == True:
            boas = card.bitoan()
            if boas==True:
                screen.fill(bg_color)
                pobito = False
                otvet = True
                atack = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if atack == False and otvet==True:
                        prov=card.otvet(screen, karta, player, 0, bg_color)
                        if prov==True:
                            pobito=True
                            otvet = False
                if event.key == pygame.K_2:
                    if atack == False and otvet==True:
                        prov= card.otvet(screen, karta, player, 1, bg_color)
                        if prov == True:
                            pobito = True
                            otvet = False
                if event.key == pygame.K_3:
                    if atack == False and otvet==True:
                        prov=card.otvet(screen, karta, player, 2, bg_color)
                        if prov == True:
                            pobito = True
                            otvet = False
                if event.key == pygame.K_4:
                    if atack == False and otvet==True:
                        prov=card.otvet(screen, karta, player, 3, bg_color)
                        if prov == True:
                            pobito = True
                            otvet = False
                if event.key == pygame.K_5:
                    if atack == False and otvet==True:
                        prov=card.otvet(screen, karta, player, 4, bg_color)
                        if prov == True:
                            pobito = True
                            otvet = False
                if event.key == pygame.K_6:
                    if atack == False and otvet==True:
                        prov=card.otvet(screen, karta, player, 5, bg_color)
                        if prov == True:
                            pobito = True
                            otvet = False
                if event.key == pygame.K_9:
                    if atack == False and otvet==True:
                        card.beru(screen,karta, player, bg_color)
                        atack = True




run()