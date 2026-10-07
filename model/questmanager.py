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