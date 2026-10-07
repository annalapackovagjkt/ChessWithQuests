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

