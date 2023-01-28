class Token:
    def __init__(self, type_, span, value):
        self.type = type_
        self.value = value
        self.span = span

    def __repr__(self):
        return f"{self.type} : {self.value}"