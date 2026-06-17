from typing import List, Dict, Any


class Quest:

    def __init__(self, id_quest: int, nazev: str, popis: str, odmena: int = 100):
        self.id_quest = id_quest
        self.nazev = nazev
        self.popis = popis
        self.odmena = odmena
        self.splneno: bool = False

    def vyhodnot(self, herni_data: Dict[str, Any]) -> bool:
        return self.splneno


class QuestManager:

    def __init__(self, field_type: str = "StandardQuests"):
        self.field_type: str = field_type
        self.seznam_questu: List[Quest] = []

    def prida_quest(self, quest: Quest) -> None:
        self.seznam_questu.append(quest)

    def skontroluj_questy(self, herni_data: Dict[str, Any]) -> List[Quest]:
        nově_splnene = []
        for q in self.seznam_questu:
            if not q.splneno and q.vyhodnot(herni_data):
                q.splneno = True
                nově_splnene.append(q)
        return nově_splnene