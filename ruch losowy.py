import random
from mapa import pokazmape
import os
import time
opcjabota = random.randint(0,3)

pole = {1: '1',2: '2',3: '3',4: '4',5: '5',
        6: '>',7: '7',8: '8',9: '9',10: '<',
        11: '11',12: '12',13: '13',14: '14',15: '15'}

niedozwolonyruch = False
tura = 0
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
    elif ruch == 'w' and pole[polegracz3] == '>':
        pole[polegracz3] = '11' 
        pole[polegracz2] = '>'
    elif ruch == 's' and pole[polegracz1] == '>':
        pole[polegracz1] = '1'
        pole[polegracz2] = '>'
    elif ruch == 's' and pole[polegracz2] == '>':
        pole[polegracz2] = '6'
        pole[polegracz3] = '>'
    elif ruch == 'p':
        pojedynek = False
    else:
        print("Nie wykonano ruchu")
        niedozwolonyruch = True
        time.sleep(3)
        tura-=1
        # dodaj wartość ograniczającą ruch 
    tura += 1
