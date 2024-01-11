

def beker():
    szam:int = int(input("Kérek egy páros számot!"))
    while szam % 2 == 0:
        return szam
    else:
        print("Nem páros szám. Kérlek adj meg egy páros számot!")

def b_feladat():
    ervenyes_szam = True
    for i in range (3):
        while ervenyes_szam:
            szam = int(input(f"Kérlek adj meg egy páros számot ({i+1}. szám): "))
            if szam % 2 == 0:
                print(f"{i+1}. szám elfogadva: {szam}")
                ervenyes_szam = False
            else:
                print("Nem páros szám. Kérlek adj meg egy páros számot!")










   
                         
                         
