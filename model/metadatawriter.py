class MetadataWriter:

    def __init__(self):
        super().__init__(field_type="metadata")
        super().__init__()

    def exportuj_metadata(self, metadata: Dict[str, Any]) -> str:
        return "\n".join([f"[{key} \"{val}\"]" for key, val in metadata.items()])
