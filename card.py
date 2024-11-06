import pygame
from socket import *
import pickle
import os

my_variable = os.getenv('HOST', 'localhost')
client = socket()

client.connect((my_variable, 4000))

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

    def hod(self, screen, razdacha, int_count):

        hod_img = pygame.image.load(razdacha[int_count][2])
        client.send(pickle.dumps(razdacha[int_count]))
        screen.blit(hod_img, (400, 300))
        razdacha.remove(razdacha[int_count])
        Card.add(self, screen, razdacha)


    def prinis(self, screen, bg_color, player):
        karta = pickle.loads(client.recv(1024))
        print(karta)
        if karta[0]=='beru':
            screen.fill(bg_color)
            if len(player)<6:
                addcard = pickle.loads(client.recv(1024))
                player.append(addcard)
            return True
        elif len(karta)==3:
            karta_img = pygame.image.load(karta[2])
            screen.blit(karta_img, (470, 300))
            return False

    def bito(self, player):
        bol="True"
        client.send(bol.encode())
        if len(player) < 6:
            addcard = pickle.loads(client.recv(1024))
            player.append(addcard)
        return False

    def prini(self, screen):
        karta = pickle.loads(client.recv(1024))
        hod_img = pygame.image.load(karta[2])
        screen.blit(hod_img, (400, 300))
        return karta

    def bitoan(self, player):
        bito1=client.recv(1024).decode()
        if bito1=='True':
            if len(player)<6:
                cards = pickle.loads(client.recv(1024))
                player.append(cards)
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