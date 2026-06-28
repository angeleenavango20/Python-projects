class Student:
    def __init__(self, name, roll_number, grades):
        student_counter = 0
        super().__init__(name)
        self.roll_number = roll_number
        self.grades = {}

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

