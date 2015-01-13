class TabeleWBazie:
    
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
            
    def stworzTabeleGatunki(self):
        sqlStworzGatunki = """CREATE TABLE IF NOT EXISTS GATUNKI (
                              Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                              Nazwa_Gatunek  CHAR(20))""" 
        try:
            self.cursor.execute(sqlStworzGatunki)   
        except Warning, e:
            print str(e)
                           
    def stworzTabeleChoroby(self):
        sqlStworzChoroby = """CREATE TABLE IF NOT EXISTS CHOROBY (
                              Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                              Nazwa_Choroba  CHAR(20))""" 
        try:
            self.cursor.execute(sqlStworzChoroby)   
        except Warning, e:
            print str(e)
         
    def stworzTabeleSpecjalizacje(self):

        sqlStworzSpecjalizacje = """CREATE TABLE IF NOT EXISTS SPECJALIZACJE (
                                    Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                    Nazwa_Specjalizacja  CHAR(20))""" 
        try:
            self.cursor.execute(sqlStworzSpecjalizacje)   
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
            
            
    def stworzTabele(self):
        
        
        self.stworzTabeleGatunki()
        self.stworzTabeleChoroby()
        self.stworzTabeleSpecjalizacje()
        self.stworzTabeleTypyZagrod()
        self.stworzTabelePozywienia()

                         

        sqlStworzZwierzeta = """CREATE TABLE IF NOT EXISTS ZWIERZETA (
                                Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                Nazwa_Zwierzecia  CHAR(20))"""
                              
        sqlLaczZwierzPoz = """CREATE TABLE IF NOT EXISTS LACZ_ZWIERZETA_POZYWIENIA (
                              Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                              ZWIERZETA_Id INT NOT NULL,
                              POZYWIENIA_Id INT NOT NULL,
                              FOREIGN KEY (ZWIERZETA_Id) REFERENCES ZWIERZETA (id) ON DELETE CASCADE ON UPDATE CASCADE,
                              FOREIGN KEY (POZYWIENIA_Id) REFERENCES POZYWIENIA(id) ON DELETE CASCADE ON UPDATE CASCADE)"""
        
        try:
            self.cursor.execute(sqlStworzZwierzeta)  
        except Warning, e:
            print str(e)
            
        try:
            self.cursor.execute(sqlLaczZwierzPoz)  
        except Warning, e:
            print str(e)
            
        
        
        