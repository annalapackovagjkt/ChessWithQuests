class RevizeTahu:

    def __init__(self, herni_plocha):
        self.herni_plocha = herni_plocha
        self.tah: list = []

    def simulate_move(self, figurka: Figurka, nova_pozice: Tuple[int, int]) -> bool:
        puvodni_pozice = figurka.get_pozice()
        figurka.posun_figurky(nova_pozice)

        vlastni_sach = self.check_sach(figurka.barva_tym)

        figurka.posun_figurky(puvodni_pozice)

        return not vlastni_sach

    def check_sach(self, barva_tym: int) -> bool:
        return False

    def check_mat(self, barva_tym: int) -> bool:
        if not self.check_sach(barva_tym):
            return False
        return False

    def check_pat(self, barva_tym: int) -> bool:
        if self.check_sach(barva_tym):
            return False
        return False

    def generuj_bezpecne_tahy(self, plocha: HerniPlocha, pozice: Tuple[int, int]) -> List[Tuple[int, int]]:
        figurka = plocha.get_figurka(pozice[0], pozice[1])
        if not figurka:
            return []

        surove_tahy = self.generuj_mozne_tahy(plocha, pozice)
        bezpecne_tahy = []

        for kam in surove_tahy:
            puvodni_fig_na_cili = plocha.get_figurka(kam[0], kam[1])
            plocha.mrizka[pozice[1]][pozice[0]] = None
            plocha.mrizka[kam[1]][kam[0]] = figurka

            if not self.check_sach(plocha, figurka.barva_tym):
                bezpecne_tahy.append(kam)

            plocha.mrizka[pozice[1]][pozice[0]] = figurka
            plocha.mrizka[kam[1]][kam[0]] = puvodni_fig_na_cili

        return bezpecne_tahy