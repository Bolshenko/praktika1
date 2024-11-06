import pickle
from socket import *
import random
import os

my_variable = os.getenv('HOST', 'localhost')

server = socket()
server.bind((my_variable, 4000))
server.listen(2)

conn1, addr1 = server.accept()
print(f"Player 1 connected.")
conn2, addr2 = server.accept()
print(f"Player 2 connected.")
player1=[]
player2=[]
hod_pervogo = True
hod_vtorogo = False
while True:
    cards = [['6', '♠', 'img/6pika.jpg'], ['7', '♠','img/pika7.jpg'], ['8', '♠','img/pika8.jpg'],
             ['9', '♠','img/pika9.jpg'], ['10', '♠','img/pika10.jpg'], ['11', '♠','img/pikaJ.jpg'],
             ['12', '♠','img/pikaQ.jpg'], ['13', '♠','img/pikaK.jpg'], ['14', '♠','img/pikaA.jpg'],
             ['6', '♥', 'img/cherva6.jpg'], ['7', '♥','img/cherva7.jpg'], ['8', '♥','img/cherva8.jpg'],
             ['9', '♥','img/cherva9.jpg'], ['10', '♥','img/cherva10.jpg'], ['11', '♥','img/chervaJ.jpg'],
             ['12', '♥','img/chervaQ.jpg'], ['13', '♥','img/chervaK.jpg'], ['14', '♥','img/chervaA.jpg'],
             ['6', '♦', 'img/bubna6.jpg'], ['7', '♦','img/bubna7.jpg'], ['8', '♦','img/bubna8.jpg'],
             ['9', '♦','img/bubna9.jpg'], ['10', '♦','img/bubna10.jpg'], ['11', '♦','img/bubnaJ.jpg'],
             ['12', '♦','img/bubnaQ.jpg'], ['13', '♦','img/bubnaK.jpg'], ['14', '♦','img/bubnaA.jpg'],
             ['6', '♣', 'img/krest6.jpg'], ['7', '♣','img/krest7.jpg'], ['8', '♣','img/krest8.jpg'],
             ['9', '♣','img/krest9.jpg'], ['10', '♣','img/krest10.jpg'], ['11', '♣','img/krestJ.jpg'],
             ['12', '♣','img/krestQ.jpg'], ['13', '♣','img/krestK.jpg'], ['14', '♣','img/krestA.jpg']]

    while len(player1) < 6:
        count = random.choice(cards)
        player1.append(count)
        cards.remove(count)
        print(player1)
    conn1.send(pickle.dumps(player1))
    while len(player2) < 6:
        count = random.choice(cards)
        player2.append(count)
        cards.remove(count)

    conn2.send(pickle.dumps(player2))
    while 1:
        while hod_pervogo:
            hod = conn1.recv(1024)
            hod_obr = pickle.loads(hod)
            player1.remove(hod_obr)
            conn2.send(hod)
            otvet = conn2.recv(1024)
            otv_beru= pickle.loads(otvet)
            if otv_beru[0]=='beru':
                player2.append(hod_obr)
                conn1.send(otvet)
                if len(player1)< 6:
                    count = random.choice(cards)
                    conn1.send(pickle.dumps(count))
                    player1.append(count)
                    cards.remove(count)
                continue
            else:
                player2.remove(otv_beru)
                conn1.send(otvet)
                bito1 = conn1.recv(1024)
                conn2.send(bito1)
                hod_vtorogo= True
                if len(player1)<6:
                    count = random.choice(cards)
                    conn1.send(pickle.dumps(count))
                    player1.append(count)
                    cards.remove(count)
                if len(player2) < 6:
                    count = random.choice(cards)
                    conn2.send(pickle.dumps(count))
                    player2.append(count)
                    cards.remove(count)
                break

        while hod_vtorogo:
            hod = conn2.recv(1024)
            hod_obr = pickle.loads(hod)
            player2.remove(hod_obr)
            conn1.send(hod)
            otvet = conn1.recv(1024)
            otv_beru= pickle.loads(otvet)
            if otv_beru[0]=='beru':
                player1.append(hod_obr)
                conn2.send(otvet)
                if len(player2)<6:
                    count = random.choice(cards)
                    conn2.send(pickle.dumps(count))
                    player2.append(count)
                    cards.remove(count)
                continue
            else:
                player1.remove(otv_beru)
                conn2.send(otvet)
                bito1 = conn2.recv(1024)
                print(bito1)
                conn1.send(bito1)
                hod_pervogo = True
                if len(player2) < 6:
                    count = random.choice(cards)
                    conn2.send(pickle.dumps(count))
                    player2.append(count)
                    cards.remove(count)
                if len(player1) < 6:
                    count = random.choice(cards)
                    conn1.send(pickle.dumps(count))
                    player1.append(count)
                    cards.remove(count)
                break
server.close()