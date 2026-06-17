from typing import List, Any, Dict

class ExportWriter:

    def __init__(self, field_type: str = "general"):
        self.field_type: str = field_type

    def write(self, data: Any) -> str:
        return str(data)


class MetadataWriter(ExportWriter):

    def __init__(self):
        super().__init__(field_type="metadata")

    def exportuj_metadata(self, metadata: Dict[str, Any]) -> str:
        return "\n".join([f"[{key} \"{val}\"]" for key, val in metadata.items()])


class ChessNotationWriter(ExportWriter):
    def __init__(self, format_notace: str = "PGN"):
        super().__init__(field_type=format_notace)
        self.format_notace: str = format_notace
        self.game_transcript: List[str] = []

    def pridat_tah(self, tah_zapis: str) -> None:
        self.game_transcript.append(tah_zapis)

    def generuj_fen(self, stav_desky: Any) -> str:
        return "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    def exportuj_pgn(self, metadata: Dict[str, Any]) -> str:
        metadata_writer = MetadataWriter()
        out = metadata_writer.exportuj_metadata(metadata) + "\n\n"

        for i in range(0, len(self.game_transcript), 2):
            cislo = (i // 2) + 1
            tah1 = self.game_transcript[i]
            tah2 = self.game_transcript[i + 1] if i + 1 < len(self.game_transcript) else ""
            out += f"{cislo}. {tah1} {tah2} "

        return out.strip()


class GameLogger:

    def __init__(self, soubor_path: str = "game.log"):
        self.soubor_path: str = soubor_path
        self.vytvor_soubor(soubor_path)

    def vytvor_soubor(self, filename: str) -> None:
        self.soubor_path = filename
        with open(self.soubor_path, "a", encoding="utf-8") as f:
            f.write("--- NOVÁ HRA ZAHÁJENA ---\n")

    def uloz_tah(self, tah: Any) -> None:
        with open(self.soubor_path, "a", encoding="utf-8") as f:
            f.write(f"Tah: {tah}\n")