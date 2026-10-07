from typing import List, Optional
from model.timer import Timer
from model.quest import QuestManager
from model.logger import GameLogger, MetadataWriter, ChessNotationWriter
from model.hrac import Hrac, Uzivatel
from model.herniplocha import HerniPlocha
from model.figurka import Figurka

class GameManager:

    def __init__(self, plocha: Optional[HerniPlocha] = None, hraci: Optional[List[Hrac]] = None):
        self.plocha: HerniPlocha = plocha if plocha else HerniPlocha()
        self.hraci: List[Hrac] = hraci if hraci else [Hrac(1, "Bílý"), Hrac(2, "Černý")]
        self.aktivni_hrac: int = 0
        self.aktualni_tah: Optional[Tah] = None

        self.casovac: Timer = Timer()
        self.game_logger: GameLogger = GameLogger("zapas.log")
        self.revizor_tahu: RevizorTahu = RevizorTahu()
        self.quest_manager: QuestManager = QuestManager()

        self.metadata_writer: MetadataWriter = MetadataWriter()
        self.chess_writer: ChessNotationWriter = ChessNotationWriter("PGN")

    def zacni_tah(self) -> Tah:
        self.aktualni_tah = Tah()
        return self.aktualni_tah

    def mozne_tahy(self) -> List[Tah]:
        return []

    def zrus_tah(self) -> None:
        self.aktualni_tah = None

    def uloz_log(self) -> None:
        if self.aktualni_tah:
            self.game_logger.uloz_tah(self.aktualni_tah)
            self.chess_writer.pridat_tah(str(self.aktualni_tah))

            self.casovac.pocitej_cas(self.aktivni_hrac)
            self.aktivni_hrac = (self.aktivni_hrac + 1) % len(self.hraci)

    def get_stav(self) -> int:
        return 0

    def najdi_uzivatele(self, id: int) -> Optional[Uzivatel]:
        for hrac in self.hraci:
            if hrac.uzivatel and hrac.uzivatel.id_uzivatele == user_id:
                return hrac.uzivatel
        return Uzivatel(id, f"Uživatel_{id}")