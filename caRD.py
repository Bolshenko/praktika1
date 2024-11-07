import pygame
from socket import *
import pickle

client = socket()

client.connect(('192.168.50.62', 4000))

class Card():

    def razdacha(self):

        data = pickle.loads(client.recv(200))
        return data

    def add(self, screen, data):
        count = 0
        x= 400
        y = 600
        while count < len(data):
            img = pygame.image.load(data[count][2])
            screen.blit(img, (x, y))
            x=x+70
            count = count+1

    def hod(self, screen, razdacha):

        hod_img = pygame.image.load(razdacha[0][2])
        razdacha.remove(razdacha[0])
        Card.add(self, screen, razdacha)
        screen.blit(hod_img, (400, 300))
        client.send(pickle.dumps(razdacha[0]))



    def prini(self, screen):
        karta = pickle.loads(client.recv(1024))
        hod_img = pygame.image.load(karta[2])
        screen.blit(hod_img, (400, 300))
        return karta

    def bitoan(self):
        bito1=client.recv(1024).decode()
        if bito1=='True':
            return True
        else:
            return False


    def otvet(self, screen, karta, player, int_count, bg_color):
        if player[int_count][1] == karta[1]:
            print("DA")
            if int(player[int_count][0]) > int(karta[0]):
                print("DA")
                screen.fill(bg_color)
                karta_1 = pygame.image.load(karta[2])
                screen.blit(karta_1, (400, 300))
                karta_2 = pygame.image.load(player[int_count][2])
                screen.blit(karta_2, (470, 300))
                client.send(pickle.dumps(player[int_count]))
                player.remove(player[int_count])
                return True
        else:
            return False

    def beru(self, screen, karta, player, bg_color):
        Beru=["beru"]
        client.send(pickle.dumps(Beru))
        player.append(karta)
        screen.fill(bg_color)




