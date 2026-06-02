class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def average(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3
    
s1 = Student("Alice", 85, 90, 95)
s2 = Student("Bob", 78, 82, 88)
print(f"{s1.name}'s average mark: {s1.average()}")
print(f"{s2.name}'s average mark: {s2.average()}")