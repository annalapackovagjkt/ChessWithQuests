class Timer:

    def __init__(self, pociatocny_cas_sekundy: int = 600):
        self.cas_hrac: List[int] = [pociatocny_cas_sekundy, pociatocny_cas_sekundy]
        self._posledni_cas: float = time.time()

    def nuluj_cas(self) -> None:
        self.cas_hrac = [0, 0]

    def pocitej_cas(self, hrac: int) -> None:
        aktualni = time.time()
        rozdil = int(aktualni - self._posledni_cas)
        if 0 <= hrac < len(self.cas_hrac):
            self.cas_hrac[hrac] = max(0, self.cas_hrac[hrac] - rozdil)
        self._posledni_cas = aktualni