class Person:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"Person: {self.name}"
    
    def __repr__(self) -> str:
        return f"Person(name='{self.name}')"