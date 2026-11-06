class ExportWriter:

    def __init__(self, field_type: str = "general"):
        self.field_type: str = field_type

    def write(self, data: Any) -> str:
        return str(data)
