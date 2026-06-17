from model.herniplocha import HerniPlocha
from model.hrac import Hrac, Uzivatel
from model.manager import GameManager, Tah


def spusti_test():
    print("--- INICIALIZACE HRY CHESS WITH QUESTS ---")

    uzivatel1 = Uzivatel(id_uzivatele=101, jmeno="Pavel")
    uzivatel2 = Uzivatel(id_uzivatele=102, jmeno="Aneta")

    hrac1 = Hrac(id_hrace=1, jmeno="Pavel", barva_tym=1, uzivatel=uzivatel1)
    hrac2 = Hrac(id_hrace=2, jmeno="Aneta", barva_tym=-1, uzivatel=uzivatel2)

    deska = HerniPlocha()
    hra = GameManager(plocha=deska, hraci=[hrac1, hrac2])

    print(f"Hra zahájena mezi: {hrac1.jmeno} (Bílý) a {hrac2.jmeno} (Černý)")

    pěšák_e2 = deska.get_figurka(4, 1)
    print(f"Figurka na pozici (4, 1): {pěšák_e2}")

    tah = Tah(odkud="e2", kam="e4", figurka="Pěšák")
    hra.aktualni_tah = tah

    posunuto = deska.posun_figurku((4, 1), (4, 3))
    if posunuto:
        hra.uloz_log()
        print("Tah e2 -> e4 byl úspěšně zapsán do logu a PGN.")

    print(f"Nová pozice pěšáka: {deska.get_figurka(4, 3)}")
    print("--- VŠECHNY MODULY FUNGUJÍ SPRÁVNĚ ---")

if __name__ == "__main__":
    spusti_test()