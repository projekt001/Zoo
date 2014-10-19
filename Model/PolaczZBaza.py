import MySQLdb
import warnings
from TabeleWBazie import TabeleWBazie
warnings.filterwarnings('error', category=MySQLdb.Warning)

# mysql -u root -p 
# password ZooBaza
mysql = MySQLdb.connect("localhost", "root", "ZooBaza", "Zoo")
tabele = TabeleWBazie(mysql)
tabele.stworzTabele()
mysql.close()