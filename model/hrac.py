class Uzivatel:

    def __init__(self, id_uzivatele: int, jmeno: str, email: str = ""):
        self.id_uzivatele: int = id_uzivatele
        self.jmeno: str = jmeno
        self.email: str = email

    def __repr__(self):
        return f"Uzivatel(id={self.id_uzivatele}, jmeno='{self.jmeno}')"


class Hrac:

    def __init__(self, id_hrace: int, jmeno: str, barva_tym: int, uzivatel: Optional[Uzivatel] = None):
        self.id_hrace: int = id_hrace
        self.jmeno: str = jmeno
        # 1 = Bílý, -1 = Černý
        self.barva_tym: int = barva_tym  
        self.uzivatel: Optional[Uzivatel] = uzivatel
        self.skore: int = 0

    def __repr__(self):
        barva = "Bílý" if self.barva_tym == 1 else "Černý"
        return f"Hrac('{self.jmeno}', barva={barva})"