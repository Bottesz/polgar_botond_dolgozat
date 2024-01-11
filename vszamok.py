import random

szam_lista = []
index = 0
while index < 13:
    vszam = random.randint(-40,150)
    szam_lista.append(vszam)
    index += 1

def veletlen_szamok():
    index = 0
    while index < len(szam_lista):
        if index < 13:
            print(f"\t{szam_lista[index]}",end=".")
        else:
            print(f"{szam_lista[index]}",end="")
        index += 1

def ketjegyuek_szama():
    index = 0 
    db = 0 
    while index < len(szam_lista):
        if szam_lista[index] < 100:
            db += 1
        index += 1
    return db

def paros_osszege():
    index = 0 
    possz = 0
    while index < len(szam_lista):
        if szam_lista[index] % 2 == 0:
            possz += 1
        index += 1
    return possz


def prtln_osszege():
    index = 0
    prtln_ossz = 0
    while index < len(szam_lista):
        if szam_lista[index] % 2 != 0:
            prtln_ossz += 1
        index += 1
    return prtln_ossz