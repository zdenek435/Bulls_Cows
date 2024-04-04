"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Zdeněk Johánek

email: zdenek.johanek@infomatic.cz

discord: zdenek0004_27578

"""
import random

def test_cisla(cislo_uzivatele):
    cislo_test = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    test_vstupu = True
    while test_vstupu:
        if (len(cislo_uzivatele) == 4):
            if cislo_uzivatele.isdigit():
                if cislo_uzivatele.startswith(cislo_test):
                    for i in cislo_uzivatele:
                        if cislo_uzivatele.count(i) > 1:
                            cislo_uzivatele = str(input("Číslo obsahuje duplicity, zadej číslo znovu:"))
                            break
                    else:
                         test_vstupu = False
                else:
                    cislo_uzivatele = str(input("Číslo nesmí začínat na 0, zadej číslo znovu:"))
            else:
                cislo_uzivatele = str(input("Číslo nesmí obsahovat jiné znaky než číslice, zadej číslo znovu:"))
        else:
            cislo_uzivatele = str(input("Číslo musí obsahovat 4 číslice, zadej číslo znovu:"))
    return cislo_uzivatele

def tisk_bull():
    if len(bull) == 1:
        tiskb = "bull"
    else:
        tiskb = "bulls"
    return tiskb

def tisk_cow():
    if len(cow) == 1:
        tiskc = "cow"
    else:
        tiskc = "cows"
    return tiskc

pomlcky = ("_" * 47)
print("Hi there!")
print(pomlcky)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(pomlcky)
uzivatel_cislo = str(input("Enter a number:"))
print(pomlcky)

vygenerovane_cislo = str(random.randint(1000, 9999))
nahodne_cislo = True
while nahodne_cislo:
    for i in vygenerovane_cislo:
        if vygenerovane_cislo.count(i) > 1:
            vygenerovane_cislo = str(random.randint(1000, 9999))
            break
    else:
        nahodne_cislo = False

print(vygenerovane_cislo)           #možnost vytisknutí hádaného čísla

bull = []
cow = []

play = True
pocet = 0
while play:
    uzivatel_cislo = test_cisla(uzivatel_cislo)
    pocet += 1
    if uzivatel_cislo == vygenerovane_cislo:
        print("Correct, you've guessed the right number\nin", pocet, "guesses!")
        print(pomlcky)
        play = False
    else:
        for poradi, cislice in enumerate(vygenerovane_cislo):
            for poradi2, cislice2 in enumerate(uzivatel_cislo):
                if poradi == poradi2 and cislice == cislice2:
                    bull.append(cislice2)
        for i in uzivatel_cislo:
            x = vygenerovane_cislo.find(i)
            if x >= 0 and bull.count(i) == 0:
                cow.append(i)
    #print(bull)
    #print(cow)
        print(len(bull), tisk_bull(), len(cow), tisk_cow())
        print(pomlcky)
        bull.clear()
        cow.clear()
        uzivatel_cislo = str(input(">>>"))

