import MySQLdb
import warnings
from TabeleWBazie import TabeleWBazie
warnings.filterwarnings('error', category=MySQLdb.Warning)

# mysql -u root -p 
# password ZooBaza

class PolaczZBaza:
    
    def __init__(self):
        self.mysql = MySQLdb.connect("localhost", "root", "ZooBaza", "Zoo")
        
    def stworzTabele(self):
        tabelewBazie = TabeleWBazie(self.mysql)
        tabelewBazie.stworzTabele()
        
    def zamknijBaze(self):
        self.mysql.close()
        
    def pobierzUchwytDoBazy(self):
        return self.mysql
    
