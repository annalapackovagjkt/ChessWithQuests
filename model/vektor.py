class Vektor:
    def __init__(self, dx: int, dy: int):
        self.dx: int = dx
        self.dy: int = dy

    def __repr__(self):
        return f"Vektor({self.dx}, {self.dy})"
