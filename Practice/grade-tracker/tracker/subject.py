class Subject:
    def __init__(self, name: str, max_marks=100):
        self.name = name
        self.max_marks = max_marks

    def __str__(self) -> str:
        return f"{self.name} (max marks: {self.max_marks})"

    def __repr__(self) -> str:
        return f"Subject(name='{self.name}', max_marks={self.max_marks})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Subject):
            return NotImplemented
        return self.name.lower() == other.name.lower()
    
    