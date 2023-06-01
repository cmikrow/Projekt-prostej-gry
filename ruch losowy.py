import random
from mapa import pokazmape
import os
import time
losowyruch = random.randint(0,2)
opcjabota = losowyruch 

pole = {1: '1',2: '2',3: '3',4: '4',5: '5',
        6: '>',7: '7',8: '8',9: '9',10: '<',
        11: '11',12: '12',13: '13',14: '14',15: '15'}

niedozwolonyruch = False
tura = 0
turabota = False
strzalwiersz1 = False
strzalwiersz2 = False
strzalwiersz3 = False
przemieszczeniepocisku1 = False
polegracz1 = 1
polegracz2 = 6
polegracz3 = 11
polebota1 = 5
polebota2 = 10
polebota3 = 15
pojedynek = True

while pojedynek:
    os.system('cls' if os.system == 'nt'  else 'clear')
    print("Tura numer: " + str(tura))
    pokazmape(pole)
    ruch = input()
    if ruch == 'w' and pole[polegracz2] == '>':
        pole[polegracz2] = '6' 
        pole[polegracz1] = '>'
        turabota == True
    elif ruch == 'w' and pole[polegracz3] == '>':
        pole[polegracz3] = '11' 
        pole[polegracz2] = '>'
        turabota == True
    elif ruch == 's' and pole[polegracz1] == '>':
        pole[polegracz1] = '1'
        pole[polegracz2] = '>'
        turabota == True
    elif ruch == 's' and pole[polegracz2] == '>':
        pole[polegracz2] = '6'
        pole[polegracz3] = '>'
        turabota == True
    elif ruch == 'd' and pole[polegracz1] == '>':
        strzalwiersz1 = True
    elif ruch == 'd' and pole[polegracz2] == '>':
        strzalwiersz2 = True
    elif ruch == 'd' and pole[polegracz3] == '>':
        strzalwiersz3 = True
    elif ruch == 'p':
        pojedynek = False
    else:
        print("Nie wykonano ruchu, ruch niedozwolony")
        niedozwolonyruch = True
        time.sleep(3)
        tura-=1
        # dodaj wartość ograniczającą ruch 
    tura += 1
    if strzalwiersz1 == True:
        pole[2] = '0'
        przemieszczeniepocisku1 = True
        if przemieszczeniepocisku1 == True and input() != '':
            pole[2] = '2'
            pole[3] = '0'
            if przemieszczeniepocisku1 == True and input() != '':
                pole[3] = '3'
                pole[4] = '0'
                if pole[4] == '0' and polebota1 == '<':
                    print("Wygrałeś")
    if strzalwiersz2 == True:
        pole[7] = '0'
        przemieszczeniepocisku1 = True
        if przemieszczeniepocisku1 == True and input() != '':
            pole[7] = '7'
            pole[8] = '0'
            if przemieszczeniepocisku1 == True and input() != '':
                pole[8] = '8'
                pole[9] = '0'
                if pole[9] == '0' and polebota2 == '<':
                    print("Wygrałeś")
    if strzalwiersz3 == True:
        pole[12] = '0'
        przemieszczeniepocisku1 = True
        if przemieszczeniepocisku1 == True and input() != '':
            pole[12] = '12'
            pole[13] = '0'
            if przemieszczeniepocisku1 == True and input() != '':
                pole[13] = '13'
                pole[14] = '0'
                if pole[14] == '0' and polebota3 == '<':
                    print("Wygrałeś")
         
    while turabota == True:
        if pole[polebota1] == '<' and opcjabota == 1:
            pole[polebota1] = '5'
            pole[polebota2] = '<'
        elif pole[polebota2] == '<' and opcjabota == 1:
            pole[polebota2] = '10'
            pole[polebota1] = '<'
        elif pole[polebota2] == '<' and opcjabota == 2:
            pole[polebota2] = '10'
            pole[polebota3] = '<'
        elif pole[polebota3] == '<' and opcjabota == 1:
            pole[polebota3] = '15'
            pole[polebota2] = '<'
        else:
            print("Bot przestał chwilowo działać :( 'nie wykonany ruch'")
    print("Ruch bota"),
    print(opcjabota)
    pokazmape(pole)
    time.sleep(3)