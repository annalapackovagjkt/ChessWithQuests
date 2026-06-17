from herniplocha import HerniPlocha, Tah

class GameManager:
    def __init__(self):
        self.plocha = HerniPlocha()
        self.aktivni_hrac = 1  # 1 pro bílého, 2 pro černého
        self.historie_tahu = []

    def proved_tah(self, tah):
        if tah.over_platnost():
            self.plocha.posun_figurku(tah)
            self.historie_tahu.append(tah)
            return True
        return False

    def get_stav(self):
        return 0