class Error:
    def __init__(self, type_, line, text, details):
        self.type = type_
        self.line = line
        self.text = text
        self.details = details

    def __repr__(self):
        return f"{self.type}Error on line {self.line}. {self.details}"
