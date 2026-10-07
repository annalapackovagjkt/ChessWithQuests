class Uzivatel:

    def __init__(self, id_uzivatele: int, jmeno: str, email: str = ""):
        self.id_uzivatele: int = id_uzivatele
        self.jmeno: str = jmeno
        self.email: str = email

    def __repr__(self):
        return f"Uzivatel(id={self.id_uzivatele}, jmeno='{self.jmeno}')"