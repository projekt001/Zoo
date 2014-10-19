import MySQLdb
import warnings
# mysql -u root -p 
# password ZooBaza

warnings.filterwarnings('error', category=MySQLdb.Warning)

# Open database connection
mysql = MySQLdb.connect("localhost", "root", "ZooBaza", "Zoo")

cursor = mysql.cursor()
sqlStworzPozywienia = """CREATE TABLE IF NOT EXISTS POZYWIENIA (
                        Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        Nazwa_Pozywienia  CHAR(20))"""

sqlStworzZwierzeta = """CREATE TABLE IF NOT EXISTS ZWIERZETA (
                        Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        Nazwa_Zwierzecia  CHAR(20))"""
                      
sqlLaczZwierzPoz = """CREATE TABLE IF NOT EXISTS LACZ_ZWIERZETA_POZYWIENIA (
                      Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                      ZWIERZETA_Id INT NOT NULL,
                      POZYWIENIA_Id INT NOT NULL,
                      FOREIGN KEY ZWIERZETA_Id(ZWIERZETA_Id) REFERENCES ZWIERZETA(id),
                      FOREIGN KEY POZYWIENIA_Id(POZYWIENIA_Id) REFERENCES POZYWIENIA(id))"""


try:
    cursor.execute(sqlStworzPozywienia)   
except Warning, e:
    print str(e)
    
try:
    cursor.execute(sqlStworzZwierzeta)  
except Warning, e:
    print str(e)
    
try:
    cursor.execute(sqlLaczZwierzPoz)  
except Warning, e:
    print str(e)
    
    
try:
    cursor.execute("""INSERT INTO POZYWIENIA(`Nazwa_Pozywienia`) VALUES('Pierogi')""")
    cursor.execute("""INSERT INTO ZWIERZETA(`Nazwa_Zwierzecia`) VALUES('Jelen')""")
except Warning, e:
    print str(e)
    
# disconnect from server
mysql.close()