class Kontroler:
    
    def __init__(self, uchwytDoBazy):
        self.uchwytDoBazy      = uchwytDoBazy;
        self.kursorDoBazy      = self.uchwytDoBazy.cursor()
        
    def zapiszWBazie(self, nazwaTabeli, opisTabeli, daneDoWstawienia):
        
        print opisTabeli
        self.iloscKolumn  = len(opisTabeli)
        komenda = "INSERT INTO " + nazwaTabeli + " ("
        
        for indexKolumny in range(1, self.iloscKolumn):
            komenda = komenda + str(opisTabeli[indexKolumny][0])
        komenda = komenda + ") VALUES("
        
    
        for indexDanych in range(len(daneDoWstawienia)):
            komenda = komenda + "'" + str(daneDoWstawienia[indexDanych]) + "'"
        komenda = komenda + ")"
        
        try:
            self.kursorDoBazy.execute(komenda)
        except Warning, e:
            print str(e)
        
    def pobierzIdPoNazwie(self,
                          nazwaTabeli,
                          nazwaKolumny,
                          wartoscPola):
        
        komenda = "SELECT * FROM " +  nazwaTabeli + \
                  " WHERE " + nazwaKolumny + " = '"+ str(wartoscPola) + "'"
        
        self.kursorDoBazy.execute(komenda)
        dane = self.kursorDoBazy.fetchall()
        return dane[0][0]
    

    def modyfikujWartoscWTabeli(self,
                                nazwaTabeli, 
                                nazwaKolumn,
                                kluczGlowny, 
                                poleDoZapisania):

        print nazwaKolumn
        komenda = "UPDATE " + str(nazwaTabeli) + " SET " 
        
        iloscKolumn = len(poleDoZapisania)
        poleDoZapisaniaLista = []
        
        for indexKolumny in range(iloscKolumn):
            chwilowaZmienna = str(poleDoZapisania[indexKolumny])
            if chwilowaZmienna.isdigit():
                poleDoZapisaniaLista.append(chwilowaZmienna)
            else:
                poleDoZapisaniaLista.append("'" + chwilowaZmienna + "'")
                
        for indexKolumny in range(iloscKolumn):
            print str(nazwaKolumn[indexKolumny + 1][0])
            komenda = komenda + str(nazwaKolumn[indexKolumny + 1][0]) + " = " + str(poleDoZapisaniaLista[indexKolumny]) + ", "
        
        komenda = komenda[0:-2] + " WHERE Id = "+ str(kluczGlowny)
        
        print komenda

        self.kursorDoBazy.execute(komenda)

    def pobierzOpisTabeli(self, nazwaTabeli):
        komenda = "DESCRIBE " + nazwaTabeli
        self.kursorDoBazy.execute(komenda)
        opisZwierzeta = self.kursorDoBazy.fetchall()
        return opisZwierzeta
    
    def pobierzWlasciweDane(self, opisZwierzeta, elementyDoUsuniecia):
        
        listaDanychDoUsuniecia = []
        nazwyKolumn            = []
        
        liczbaKolumn = len(opisZwierzeta)
        for indexKolumny in range(liczbaKolumn):
            if ( self.znajdzElementWLiscie(elementyDoUsuniecia, opisZwierzeta[indexKolumny][0])):
                listaDanychDoUsuniecia.append(indexKolumny)
            else:
                nazwyKolumn.append(str(opisZwierzeta[indexKolumny][0]))
        return listaDanychDoUsuniecia, nazwyKolumn
    
    
    def pobierzDane(self, nazwaTabeli):
        komenda = "SELECT * FROM " +  nazwaTabeli
        self.kursorDoBazy.execute(komenda)
        daneZwierzeta = self.kursorDoBazy.fetchall()
                
        return daneZwierzeta
    
    def pobierzJedenWiersz(self, nazwaTabeli, kluczGlowny):
        print 'Jeden Wiersz !'
        komenda = "SELECT * FROM " +  nazwaTabeli + " WHERE Id =" + str(kluczGlowny)
        self.kursorDoBazy.execute(komenda)
        dane = self.kursorDoBazy.fetchone()
                
        return dane
    
    
    def laczTabeleIPobierzWiersz(self, 
                                 tabelaGlowna, 
                                 tabelaDoDolaczenia, 
                                 nazwaKluczaGlowna, 
                                 nazwaKluczaDolaczenia, 
                                 nazwaKolumnyDolaczenia,
                                 kluczGlowny):

        komenda  = "SELECT " +  tabelaGlowna + ".*, " + tabelaDoDolaczenia + "." + nazwaKolumnyDolaczenia + " FROM " + tabelaGlowna + \
                   " LEFT JOIN " + tabelaDoDolaczenia + \
                   " ON " + tabelaGlowna + "." + nazwaKluczaGlowna + " = " + tabelaDoDolaczenia + "." + nazwaKluczaDolaczenia + \
                   " WHERE " + tabelaGlowna + ".Id =" + str(kluczGlowny)
                   
        self.kursorDoBazy.execute(komenda)
        
        return self.kursorDoBazy.fetchone()
    
    def znajdzElementWLiscie(self, znaczniki, element):
        return [item for item in range(len(znaczniki)) if znaczniki[item] == element]

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
            
            self.kursorDoBazy.execute("""INSERT INTO ZAGRODY (Powierzchnia, TYPY_ZAGROD_Id)   
                                                             VALUES(90, 1)""")
                           
            self.kursorDoBazy.execute("""INSERT INTO ZWIERZETA (Nazwa_Zwierzecia, Wzrost, Waga, Wiek, GATUNEK_Id, ZAGRODA_Id) 
                                                               VALUES('Hipopotam', 120, 10, 20, 1, 1)""")
            self.kursorDoBazy.execute("""INSERT INTO ZWIERZETA (Nazwa_Zwierzecia, Wzrost, Waga, Wiek, GATUNEK_Id, ZAGRODA_Id) 
                                                               VALUES('Zyrafa', 55, 10, 20, 2, 2)""")
            self.kursorDoBazy.execute("""INSERT INTO ZWIERZETA (Nazwa_Zwierzecia, Wzrost, Waga, Wiek, GATUNEK_Id, ZAGRODA_Id) 
                                                               VALUES('Tygrys', 90, 10, 20, 2, 2)""")
            

        except Warning, e:
            print str(e)
            
    def laczTabele(self, tabelaGlowna, tabelaDoDolaczenia, nazwaKluczaGlowna, nazwaKluczaDolaczenia, nazwaKolumnyDolaczenia):

        komenda  = "SELECT " +  tabelaGlowna + ".*, " + tabelaDoDolaczenia + "." + nazwaKolumnyDolaczenia + " FROM " + tabelaGlowna + \
                   " LEFT JOIN " + tabelaDoDolaczenia + \
                   " ON " + tabelaGlowna + "." + nazwaKluczaGlowna + " = " + tabelaDoDolaczenia + "." + nazwaKluczaDolaczenia
        self.kursorDoBazy.execute(komenda)
        
        
        return self.kursorDoBazy.fetchall()
        
        
        