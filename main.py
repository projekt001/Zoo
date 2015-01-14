import sys
sys.path.append("Controler")
sys.path.append("Model")
sys.path.append("View")

from GlowneOkno import GlowneOkno
from PolaczZBaza import PolaczZBaza
from Kontroler import Kontroler

if __name__ == "__main__":
    polaczZBaza = PolaczZBaza()
    polaczZBaza.stworzTabele()
    uchwytDoBazy = polaczZBaza.pobierzUchwytDoBazy()
    
    kontroler  = Kontroler(uchwytDoBazy)
    kontroler.dodajRekordy()
    glowneOkno = GlowneOkno(uchwytDoBazy)

    polaczZBaza.zamknijBaze()
    