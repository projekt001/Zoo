class TabeleWBazie:
    
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
            
    def stworzTabeleGatunki(self):
        sqlStworzGatunki = """CREATE TABLE IF NOT EXISTS GATUNKI (
                              Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                              Nazwa_Gatunku CHAR(20))""" 
        try:
            self.cursor.execute(sqlStworzGatunki)   
        except Warning, e:
            print str(e)
                           
    def stworzTabeleChoroby(self):
        sqlStworzChoroby = """CREATE TABLE IF NOT EXISTS CHOROBY (
                              Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                              Nazwa_Choroby  CHAR(20))""" 
        try:
            self.cursor.execute(sqlStworzChoroby)   
        except Warning, e:
            print str(e)
            
    def stworzTabeleTypyZagrod(self):
                
        sqlStworzTypyZagrod = """CREATE TABLE IF NOT EXISTS TYPY_ZAGROD (
                                 Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                 Nazwa_Typ_Zagrody  CHAR(20))""" 
                                 
        try:
            self.cursor.execute(sqlStworzTypyZagrod)   
        except Warning, e:
            print str(e)
            
    def stworzTabelePozywienia(self):
        
        sqlStworzPozywienia = """CREATE TABLE IF NOT EXISTS POZYWIENIA (
                                 Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                 Nazwa_Pozywienia  CHAR(20))"""
        try:
            self.cursor.execute(sqlStworzPozywienia)   
        except Warning, e:
            print str(e)

    def stworzTabeleZagrody(self):
        
        sqlStworzZagrody = """CREATE TABLE IF NOT EXISTS ZAGRODY (
                              Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                              Nazwa_Zagrody CHAR(20),
                              Powierzchnia INT NOT NULL,
                              TYPY_ZAGROD_Id INT NOT NULL,
                              FOREIGN KEY (TYPY_ZAGROD_Id) REFERENCES TYPY_ZAGROD(Id))"""

        try:
            self.cursor.execute(sqlStworzZagrody)   
        except Warning, e:
            print str(e)
            
    def stworzTabeleZwierzeta(self):
        
        sqlStworzZwierzeta = """CREATE TABLE IF NOT EXISTS ZWIERZETA (
                                Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                Nazwa_Zwierzecia  CHAR(20),
                                Wzrost INT NOT NULL,
                                Waga INT NOT NULL,
                                Wiek INT NOT NULL,
                                GATUNEK_Id INT NOT NULL,
                                ZAGRODA_Id INT NOT NULL,
                                FOREIGN KEY (GATUNEK_Id) REFERENCES GATUNKI(Id),
                                FOREIGN KEY (ZAGRODA_Id) REFERENCES ZAGRODY(Id))"""

        try:
            self.cursor.execute(sqlStworzZwierzeta)   
        except Warning, e:
            print str(e)
            
    def stworzTabeleLaczZwierzPoz(self):
        sqlLaczZwierzPoz = """CREATE TABLE IF NOT EXISTS LACZ_ZWIERZETA_POZYWIENIA (
                              Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                              ZWIERZETA_Id INT NOT NULL,
                              POZYWIENIA_Id INT NOT NULL,
                              FOREIGN KEY (ZWIERZETA_Id) REFERENCES ZWIERZETA (Id) ON DELETE CASCADE ON UPDATE CASCADE,
                              FOREIGN KEY (POZYWIENIA_Id) REFERENCES POZYWIENIA (Id) ON DELETE CASCADE ON UPDATE CASCADE)"""
        
            
        try:
            self.cursor.execute(sqlLaczZwierzPoz)  
        except Warning, e:
            print str(e)
            
    def stworzTabeleLaczChorZwierz(self):
        sqlLaczChorobyZwierz = """CREATE TABLE IF NOT EXISTS LACZ_ZWIERZETA_CHOROBY (
                                  Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                  ZWIERZETA_Id INT NOT NULL,
                                  CHOROBY_Id INT NOT NULL,
                                  FOREIGN KEY (ZWIERZETA_Id) REFERENCES ZWIERZETA (Id) ON DELETE CASCADE ON UPDATE CASCADE,
                                  FOREIGN KEY (CHOROBY_Id) REFERENCES CHOROBY (Id) ON DELETE CASCADE ON UPDATE CASCADE)"""
        
            
        try:
            self.cursor.execute(sqlLaczChorobyZwierz)  
        except Warning, e:
            print str(e)
            
    def stworzTabeleLaczChorZwierz(self):
        sqlLaczChorobyZwierz = """CREATE TABLE IF NOT EXISTS LACZ_ZWIERZETA_CHOROBY (
                                  Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                  ZWIERZETA_Id INT NOT NULL,
                                  CHOROBY_Id INT NOT NULL,
                                  FOREIGN KEY (ZWIERZETA_Id) REFERENCES ZWIERZETA (Id),
                                  FOREIGN KEY (CHOROBY_Id) REFERENCES CHOROBY (Id))"""
        
            
        try:
            self.cursor.execute(sqlLaczChorobyZwierz)  
        except Warning, e:
            print str(e)
            
    def stworzTabeleSpecjalizacje(self):
        sqlSpecjalizacje = """CREATE TABLE IF NOT EXISTS SPECJALIZACJE (
                                  Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                  Nazwa_Specjalizacji CHAR(20))"""
        
            
        try:
            self.cursor.execute(sqlSpecjalizacje)  
        except Warning, e:
            print str(e)
            
    def stworzTabeleWeterynarze(self):
        sqlWeterynarze = """CREATE TABLE IF NOT EXISTS WETERYNARZE (
                                  Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                  Imie CHAR(20),
                                  Nazwisko CHAR(20),
                                  Wiek INT NOT NULL,
                                  SPECJALIZACJE_Id INT NOT NULL,
                                  FOREIGN KEY (SPECJALIZACJE_Id) REFERENCES SPECJALIZACJE (Id))"""
        
            
        try:
            self.cursor.execute(sqlWeterynarze)  
        except Warning, e:
            print str(e)
            
    def stworzTabeleLaczZagrodyWeterynarze(self):
        
        sqlLaczWetZag = """CREATE TABLE IF NOT EXISTS LACZ_ZAGRODY_WETERYNARZE (
                           Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                           ZAGRODY_Id INT NOT NULL,
                           WETERYNARZE_Id INT NOT NULL,
                           FOREIGN KEY (ZAGRODY_Id) REFERENCES ZAGRODY (Id),
                           FOREIGN KEY (WETERYNARZE_Id) REFERENCES WETERYNARZE (Id))"""
        try:
            self.cursor.execute(sqlLaczWetZag)  
        except Warning, e:
            print str(e)
              
            
    def stworzTabele(self):
        
        self.usunJesliIstnieja()
        
        
        self.stworzTabeleGatunki()
        self.stworzTabeleChoroby()
        self.stworzTabeleTypyZagrod()
        self.stworzTabelePozywienia()
        self.stworzTabeleZagrody()
        self.stworzTabeleZwierzeta()
        self.stworzTabeleLaczZwierzPoz()
        self.stworzTabeleLaczChorZwierz()
        self.stworzTabeleSpecjalizacje()                   
        self.stworzTabeleWeterynarze()
        self.stworzTabeleLaczZagrodyWeterynarze()    
          
    def usunJesliIstnieja(self):

        try:
            self.cursor.execute("DROP TABLE IF EXISTS LACZ_ZAGRODY_WETERYNARZE")
        except Warning, e:
            print str(e)
            
        try:
            self.cursor.execute("DROP TABLE IF EXISTS WETERYNARZE")
        except Warning, e:
            print str(e)
            
        try:
            self.cursor.execute("DROP TABLE IF EXISTS SPECJALIZACJE")
        except Warning, e:
            print str(e)
            
        try:
            self.cursor.execute("DROP TABLE IF EXISTS LACZ_ZWIERZETA_CHOROBY")
        except Warning, e:
            print str(e)
            
        try:
            self.cursor.execute("DROP TABLE IF EXISTS CHOROBY")
        except Warning, e:
            print str(e)
            
        try:
            self.cursor.execute("DROP TABLE IF EXISTS LACZ_ZWIERZETA_POZYWIENIA")
        except Warning, e:
            print str(e)
            
        try:
            self.cursor.execute("DROP TABLE IF EXISTS POZYWIENIA")
        except Warning, e:
            print str(e)
            
        try:
            self.cursor.execute("DROP TABLE IF EXISTS ZWIERZETA")
        except Warning, e:
            print str(e)
            
            
        try:
            self.cursor.execute("DROP TABLE IF EXISTS GATUNKI")
        except Warning, e:
            print str(e)
            
        try:
            self.cursor.execute("DROP TABLE IF EXISTS ZAGRODY")
        except Warning, e:
            print str(e)
            
           
        try:
            self.cursor.execute("DROP TABLE IF EXISTS TYPY_ZAGROD")
        except Warning, e:
            print str(e)


           
        
        
        