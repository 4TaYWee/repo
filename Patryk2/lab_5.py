

import random
import scipy.special as sc


def runs_test(ciag):
    n = len(ciag)
    ciagg = ''.join(map(str, ciag))
    n = len(ciagg)
    przebiegi = [0] * 20
    aktualny = 1
    for i in range(1,n):
        if ciag[i] != ciag[i-1]:
            przebiegi[aktualny] += 1
            aktualny = 1;
        else:
            aktualny += 1
    przebiegi[aktualny] += 1

    print(przebiegi)
#    print(przebiegi[5])
#    print(przebiegi[4])
#    print(przebiegi[3])
#    print(przebiegi[2])
#    print(przebiegi[1])

    flaga1 = 0
    flaga2 = 0
    flaga3 = 0
    flaga4 = 0
    flaga5 = 0
    flaga6 = 0
    if przebiegi[6] > 2685 and przebiegi[6]< 2315:
        flaga1 = 1
    if przebiegi[5] > 2685 and przebiegi[5] < 2315:
        flaga2 = 1
    if przebiegi[4] > 2685 and przebiegi[4] < 2315:
        flaga3 = 1
    if przebiegi[3] > 2685 and przebiegi[3] < 2315:
        flaga4 = 1
    if przebiegi[2] > 2685 and przebiegi[2] < 2315:
        flaga5 = 1
    if przebiegi[1] > 2685 and przebiegi[1] < 2315:
        flaga6 = 1

    if flaga1 * flaga2 * flaga3 * flaga4 * flaga5 * flaga6 == 0:
        return "test runs test nieudany"
    else:
        return "test runs test udany"

'''
    print("6 bitow occurrence: ", ciag.count('000000') + ciag.count('1111111'))
    print("5 occurrence: ", ciag.count('00000') + ciag.count('11111'))
    print("4 occurrence: ", ciag.count('0000') + ciag.count('1111'))
    print("3 occurrence: ", ciag.count('000') + ciag.count('111'))
    print("2 occurrence: ", ciag.count('00') + ciag.count('11'))
    print("1 occurrence: ", ciag.count('0') + ciag.count('1'))
'''

def Inicjuj_losowy_ciag(dlugosc):
    ciag = []

    for i in range(dlugosc):
        ciag.append(random.randint(0, 1))
    #ciag = int("".join(map(str, ciag)))
    return ciag

def znajdz_funkcje_dla_ciagu(funkcja):
    for i, c in enumerate(funkcja):
        if c == 1:
            numery.append(i)
    return numery

def rejestr_przesuwny(dlugosc_ciagu,wyraz_wolny,funkcja):
    for i in range(dlugosc_ciagu):
        # print(i)
        if i == 0:
            xor = funkcja[i] ^ wyraz_wolny
            #print("funkcja [i] = ", funkcja[i])
        if i != numery[-1:]:  # wszystko przed ostatnim elementem ze wzgledu na i+1
            xor = xor ^ funkcja[i + 1]
            #print("funkcja xor = ", xor)
            #print("funkcja [i+1] = ", funkcja[i+1])
        return xor







def przesun(funkcja,xor):
    funkcja.pop(0)
    funkcja.extend([xor])
    return funkcja

def poker_test(ciag):
    # podzielone w 4 bitowe paczki
    packs = [ciag[i:i + 4] for i in range(0, len(ciag), 4)]

    # ilosc 4 bitowych paczek
    count = {}
    for pack in packs:
        pack_str = "".join(str(bit) for bit in pack)
        if pack_str in count:
            count[pack_str] += 1
        else:
            count[pack_str] = 1

    #Procenty pokerowe
    N = len(packs)
    f = list(count.values())
    X = (16 / N) * sum([f_ele ** 2 for f_ele in f]) - N

    return N,f,X

def long_runs_test(ciag):
        zero = "0" * 26
        jeden = "1" * 26
        ciag_str = "".join(str(bit) for bit in ciag)

        if zero in ciag_str or jeden in ciag_str:
            return "Test nieudany"
        else:
            return "Test udany"


dlugosc_LFSR = 13*2*2*2
dlugosc_LFSR2 = 14*2*2*2
dlugosc_LFSR3 = 8*2*2*2

wyraz_wolny = 1
wyraz_wolny2 = 0
wyraz_wolny3 = 1


funkcja = Inicjuj_losowy_ciag(dlugosc_LFSR)
funkcja2 = Inicjuj_losowy_ciag(dlugosc_LFSR2)
funkcja3 = Inicjuj_losowy_ciag(dlugosc_LFSR3)
print(funkcja)

numery = []
numery2 = []
numery3 = []

numery = znajdz_funkcje_dla_ciagu(funkcja)
numery2 = znajdz_funkcje_dla_ciagu(funkcja2)
numery3 = znajdz_funkcje_dla_ciagu(funkcja3)


print(numery)

wynik_xor = []
wynik_xor2 = []
wynik_xor3 = []

num = len(numery)
num2 = len(numery)
num3 = len(numery)

ciag_losowy = []
ciag_losowy2 = []
ciag_losowy3 = []

gef_wyjscie = []

for i in range(20000):
    xor = rejestr_przesuwny(num,wyraz_wolny,funkcja)
    ciag_losowy.append(xor)
    #print(xor)
        #dodanie wyniku na sam koniec i usuniecie pierwszego elementu
    funkcja = przesun(funkcja,xor)
    #print(funkcja)



    xor2 = rejestr_przesuwny(num2,wyraz_wolny2,funkcja2)
    ciag_losowy2.append(xor2)
    #print(xor)
        #dodanie wyniku na sam koniec i usuniecie pierwszego elementu
    funkcja2 = przesun(funkcja2,xor2)
    #print(funkcja)



    xor3 = rejestr_przesuwny(num3,wyraz_wolny3,funkcja3)
    ciag_losowy3.append(xor3)
    #print(xor)
        #dodanie wyniku na sam koniec i usuniecie pierwszego elementu
    funkcja3 = przesun(funkcja3,xor3)
    #print(funkcja)

    ###------Generator Geffe'go---###
    gef_x1 = xor & xor2
    gef_x2 = ~xor & xor3
    gef_wynik = gef_x1 ^ gef_x2
    gef_wyjscie.append(gef_wynik)


print(ciag_losowy)
print(ciag_losowy2)
print(ciag_losowy3)
print("gef = ",gef_wyjscie)


#Poker test
print("LFSR 1: poker_test ", poker_test(ciag_losowy))
print("LFSR 2: poker_test ", poker_test(ciag_losowy2))
print("LFSR 3: poker_test ", poker_test(ciag_losowy3))
print("gef: poker_test ", poker_test(gef_wyjscie))

#long_runs_test:
print("LFSR 1 long:", long_runs_test(ciag_losowy))
print("LFSR 2 long :", long_runs_test(ciag_losowy2))
print("LFSR 3 long :", long_runs_test(ciag_losowy3))
print("gef long :", long_runs_test(gef_wyjscie))


print("LFSR 1: runs_test ", runs_test(ciag_losowy))
print("LFSR 2: runs_test ", runs_test(ciag_losowy2))
print("LFSR 3: runs_test ", runs_test(ciag_losowy3))
print("gef: runs_test ", runs_test(gef_wyjscie))
'''
ZAD 8.2
Dla testu pokerowego generatory o wiele częściej nie spelniały wymowgów testu pokerowego, przy wielokrotnych probach
Dla testu long_runs test nie wystąpiły żadne zmiany
Zwiększenie ilości bitów ciągu zwiększa szansę na niepowodzenie wykonania testu
Dla 16-krotnego zwiekszenia dlugosci LFSR zauważono poprawę dla testu pokerowego, reszta nie miala zmian

'''
