class Kontroler:
    
    def __init__(self, uchwytDoBazy):
        self.uchwytDoBazy      = uchwytDoBazy;
        self.kursorDoBazy      = self.uchwytDoBazy.cursor()
        
    def dodajRekordy(self):
        try:
            self.kursorDoBazy.execute("""INSERT INTO POZYWIENIA (Nazwa_Pozywienia) VALUES('Buraki')""")
            self.kursorDoBazy.execute("""INSERT INTO POZYWIENIA (Nazwa_Pozywienia) VALUES('Marchew')""")
            self.kursorDoBazy.execute("""INSERT INTO POZYWIENIA (Nazwa_Pozywienia) VALUES('JABLKA')""")
            
            self.kursorDoBazy.execute("""INSERT INTO CHOROBY (Nazwa_Choroby) VALUES('Slepota')""")
            self.kursorDoBazy.execute("""INSERT INTO CHOROBY (Nazwa_Choroby) VALUES('Martwota')""")
            self.kursorDoBazy.execute("""INSERT INTO CHOROBY (Nazwa_Choroby) VALUES('Cukrzyca')""")
            
            self.kursorDoBazy.execute("""INSERT INTO GATUNKI (Nazwa_Gatunku) VALUES('Malpa')""")
            self.kursorDoBazy.execute("""INSERT INTO GATUNKI (Nazwa_Gatunku) VALUES('Kon')""")
            self.kursorDoBazy.execute("""INSERT INTO GATUNKI (Nazwa_Gatunku) VALUES('Gepard')""")
            
            self.kursorDoBazy.execute("""INSERT INTO TYPY_ZAGROD (Nazwa_Typ_Zagrody) VALUES('Mala')""")
            self.kursorDoBazy.execute("""INSERT INTO TYPY_ZAGROD (Nazwa_Typ_Zagrody) VALUES('Duza')""")
            self.kursorDoBazy.execute("""INSERT INTO TYPY_ZAGROD (Nazwa_Typ_Zagrody) VALUES('Wielka')""")
            
            self.kursorDoBazy.execute("""INSERT INTO ZAGRODY (Powierzchnia, TYPY_ZAGROD_Id)   
                                                             VALUES(15, 1)""")
            self.kursorDoBazy.execute("""INSERT INTO ZAGRODY (Powierzchnia, TYPY_ZAGROD_Id)   
                                                             VALUES(40, 2)""")
            self.kursorDoBazy.execute("""INSERT INTO ZAGRODY (Powierzchnia, TYPY_ZAGROD_Id)   
                                                             VALUES(90, 3)""")
                           
            self.kursorDoBazy.execute("""INSERT INTO ZWIERZETA (Nazwa_Zwierzecia, Wzrost, Waga, Wiek, GATUNEK_Id, ZAGRODA_Id) 
                                                               VALUES('Hipopotam', 120, 10, 20, 1, 1)""")
            self.kursorDoBazy.execute("""INSERT INTO ZWIERZETA (Nazwa_Zwierzecia, Wzrost, Waga, Wiek, GATUNEK_Id, ZAGRODA_Id) 
                                                               VALUES('Zyrafa', 55, 10, 20, 2, 2)""")
            self.kursorDoBazy.execute("""INSERT INTO ZWIERZETA (Nazwa_Zwierzecia, Wzrost, Waga, Wiek, GATUNEK_Id, ZAGRODA_Id) 
                                                               VALUES('Tygrys', 90, 10, 20, 2, 2)""")
            

        except Warning, e:
            print str(e)