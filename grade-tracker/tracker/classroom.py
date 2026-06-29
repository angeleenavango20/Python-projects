from .student import Student
from .subject import Subject
import json

class Classroom:
    def __init__(self, class_name: str):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        for existing in self.students:
            if existing == student:  # calls Student.__eq__ 
                raise ValueError(f"Student with roll number {student.roll_number} already exists.")
        self.students.append(student)

    def remove_student(self, roll_number):
        student = self.get_student(roll_number)
        self.students.remove(student)
        return student
        
    def get_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        raise ValueError(f"Student with roll number {roll_number} not found.")
    
    def get_topper(self):
        if not self.students:
            raise ValueError("Classroom is empty.")
        return max(self.students, key=lambda student: student.get_percentage())
    
    def get_rankings(self):
        return sorted(self.students, key=lambda student: student.get_percentage(), reverse=True)
    
    def print_summary(self):
        print(f"Classroom: {self.class_name}")
        print("-" * 40)
        print(f"{'Name':<20} {'Roll No':<10} {'Percentage':>10}")
        print("-" * 40)
        for student in self.students:
            percentage = student.get_percentage()
            print(f"{student.name:<20} {student.roll_number:<10} {percentage:>10.2f}%")
        print("-" * 40)
        topper = self.get_topper()
        print(f"Topper: {topper.name} (Roll No: {topper.roll_number}) with {topper.get_percentage():.2f}%")

    def save_to_json(self, filepath):
        data = {
            "class_name": self.class_name,
            "students": [
                {
                    "name": student.name,
                    "roll_number": student.roll_number,
                    "grades": {subject.name: { "marks": marks , "max_marks": subject.max_marks } for subject, marks in student.grades.items()}
                }
                for student in self.students
            ]
        }
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_json(self, filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.class_name = data["class_name"]
        self.students = []
        for student_data in data["students"]:
            student = Student(student_data["name"], student_data["roll_number"])
            for subject_name, grade_data in student_data["grades"].items():
                subject = Subject(subject_name, grade_data["max_marks"]) 
                student.add_grade(subject, grade_data["marks"])
            self.students.append(student)

    def __str__(self):
        return f"Classroom: {self.class_name} ({len(self.students)} students)"
    
    def __len__(self):
        return len(self.students)
    