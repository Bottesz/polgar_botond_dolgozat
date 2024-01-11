class f1_adatok:
    def __init__(self,sor:str):
        adatok = sor.strip().split("!")
        self.stadion_nev = str(adatok[0])
        self.stadion_helyszinenek_varosa = str(adatok[1])
        self.stadionnak_hanyas_csapata = int(adatok[2])
        self.mikor_leptek_eloszor = int(adatok[3])
        self.mikor_leptek_utoljara = int(adatok[4])

    def __str__(self):
        return f"stadion: {self.stadion_nev}, város: {self.stadion_helyszinenek_varosa}, csapat: {self.stadionnak_hanyas_csapata}, első mérkőzés: {self.mikor_leptek_eloszor}, utolsó mérkőzés: {self.mikor_leptek_utoljara}"