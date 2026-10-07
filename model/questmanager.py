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

    def __init__(self):
        self.dostupne_questy = [
            Quest(1, "První krev", "Vyhoď první soupeřovu figurku", odmena=50),
            Quest(2, "Jezdecký výpad", "Táhni Koněm do soupeřovy poloviny", odmena=100)
        ]

    def vyhodnot_po_tahu(self, tah, vyhozena_figurka=None):
        for quest in self.dostupne_questy:
            if not quest.splneno:
                if quest.id_quest == 1 and vyhozena_figurka is not None:
                    quest.splneno = True
                    print(f"Quest splněn: {quest.nazev}!")