import forma1
f = open("stadionok.txt","r",encoding="utf-8" )
f.readline()
sorok = f.readlines()
f.close()

def csapatok_szama():
    csapatok_szama = 0
    index = 0 
    while index < len(sorok):
        csapatok_szama += 1
        index += 1
    print(f"\n\t A csapatok db száma: {index}")

def csapat_kiiras():
    stadionok = []
    for sor in sorok[1:]:
        data = sor.strip().split(";")
        stadionok.append
        csapat:[0]
        varos: [1]
        csapatok_szama: int(data[2])