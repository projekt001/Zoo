import sys
sys.path.append("Kontroler")
sys.path.append("Model")
sys.path.append("View")

from GlowneOkno import GlowneOkno
from PolaczZBaza import PolaczZBaza

if __name__ == "__main__":
    polaczZBaza = PolaczZBaza()
    polaczZBaza.stworzTabele()
    uchwytDoBazy = polaczZBaza.pobierzUchwytDoBazy()
    glowneOkno = GlowneOkno(uchwytDoBazy)
    polaczZBaza.zamknijBaze()
    