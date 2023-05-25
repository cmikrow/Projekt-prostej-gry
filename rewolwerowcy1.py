import keyboard
import random
# while True:
#     if keyboard.press_and_release("w"):
#         print("You pressed 'w'.")
#     break
tury = 1
pozycjagracza = 2
pozycjabota = 2
gracz = ">"
bot = "<"
pustepole = "|"
ppolegracz1 = "|"
ppolegracz2 = ">"
ppolegracz3 = "|"
ppolebot1 = "|"
ppolebot2 = "<"
ppolebot3 = "|"
wiersz1 = 0,0,0,0,0
wiersz2 = 0,0,0,0,0
wiersz3 = 0,0,0,0,0
pocisk = '-'
# if pocisk in wiersz1:
#     print("p wierszu1")
# else:
#     print("p' wierszu1")

# Gracz

if keyboard.press_and_release("w") and pozycjagracza == 2:
    ppolegracz1 = ppolegracz2
    ppolegracz2 = pustepole
if keyboard.press_and_release("w") and pozycjagracza == 3:
    ppolegracz2 = ppolegracz3
    ppolegracz3 = pustepole
if keyboard.press_and_release("s") and pozycjagracza == 1:
    ppolegracz2 = ppolegracz1
    ppolegracz1 = pustepole
if keyboard.press_and_release("s") and pozycjagracza == 2:
    ppolegracz3 = ppolegracz2
    ppolegracz2 = pustepole
if keyboard.press_and_release("s") and pozycjagracza == 1 and '-' not in wiersz1:
    wiersz1 = "-,0,0,0,0"
if keyboard.press_and_release("s") and pozycjagracza == 2 and '-' not in wiersz2: 
    wiersz2 = "-,0,0,0,0"
if keyboard.press_and_release("s") and pozycjagracza == 3 and '-' not in wiersz3:
    wiersz3 = "-,0,0,0,0"

# Bot
wyborbota = 1,2,3
if random.choice(wyborbota) == 1 and pozycjabota == 2:
    ppolebot1 = ppolebot2
    ppolebot2 = pustepole
if random.choice(wyborbota) == 1 and pozycjabota == 3:
    ppolebot2 = ppolebot3
    ppolebot3 = pustepole
if random.choice(wyborbota) == 2 and pozycjabota == 1:
    ppolebot2 = ppolebot1
    ppolebot1 = pustepole
if random.choice(wyborbota) == 2 and pozycjabota == 2:
    ppolebot3 = ppolebot2
    ppolebot2 = pustepole
if random.choice(wyborbota) == 3 and pozycjagracza == 1 and '-' not in wiersz1:
    wiersz1 = "0,0,0,0,-"
if random.choice(wyborbota) == 3 and pozycjagracza == 2 and '-' not in wiersz2:
    wiersz2 = "0,0,0,0,-"
if random.choice(wyborbota) == 3 and pozycjagracza == 3 and '-' not in wiersz3:
    wiersz3 = "0,0,0,0,-"

linijka1 = f" {ppolegracz1}{wiersz1}{ppolebot1}"
linijka2 = f" {ppolegracz2}{wiersz2}{ppolebot2}"
linijka3 = f" {ppolegracz3}{wiersz3}{ppolebot3}"

if tury == 1:
    print(linijka1)
    print(linijka2)
    print(linijka3)
# if keyboard.press_and_release("w") or keyboard.press_and_release("s") or keyboard.press_and_release("d"): 
# print("\n")
# for pocisk in wiersz2:
#     print("p wierszu2")
# for pocisk in wiersz3:
#     print("p wierszu3")

