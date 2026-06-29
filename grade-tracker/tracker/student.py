class Student(Person):
    student_counter = 0
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number
        self.grades = {}
        Student.student_counter += 1

    def add_grade(self, subject, marks):
        if marks < 0 or marks > subject.max_marks:
            raise ValueError(f"Marks should be between 0 and {subject.max_marks}")
        self.grades[subject] = marks

    def get_average(self):
        if not self.grades:
            return 0.0
        total_marks = sum(self.grades.values())
        return total_marks / len(self.grades)
    
    def get_percentage(self):
        if not self.grades:
            return 0.0
        total_marks = sum(self.grades.values())
        total_max_marks = sum(subject.max_marks for subject in self.grades.keys())
        return (total_marks / total_max_marks) * 100

    def print_report_card(self):
        print("-" * 40)
        print(f"Report Card — {self.name} (Roll No: {self.roll_number})")
        print("-" * 40)
        for subject, marks in self.grades.items():
            print(f"{subject.name:<12}: {marks:>3} / {subject.max_marks}")
        print("-" * 40)
        average = self.get_average()
        percentage = self.get_percentage()
        print(f"Average      : {average:.2f}")
        print(f"Percentage   : {percentage:.2f}%")
        print("-" * 40)

    def __str__(self):
        return f"Student: {self.name} (Roll No: {self.roll_number})"
    
    def __repr__(self):
        return f"Student(name='{self.name}', roll_number={self.roll_number})"
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.roll_number == other.roll_number
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_percentage() < other.get_percentage()
