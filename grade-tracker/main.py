from tracker import Student, Subject, Classroom


def main():

    # 1. CREATE THE CLASSROOM
    classroom = Classroom("Class 10A")

    # 2. CREATE SUBJECTS
    maths   = Subject("Maths", 100)
    science = Subject("Science", 100)
    english = Subject("English", 100)

    # 3. CREATE STUDENTS
    arjun = Student("Arjun", 1)
    priya = Student("Priya", 2)
    rahul = Student("Rahul", 3)

    # 4. ADD STUDENTS TO CLASSROOM
    classroom.add_student(arjun)
    classroom.add_student(priya)
    classroom.add_student(rahul)

    # 5. ADD GRADES
    arjun.add_grade(maths, 88)
    arjun.add_grade(science, 76)
    arjun.add_grade(english, 91)

    priya.add_grade(maths, 95)
    priya.add_grade(science, 89)
    priya.add_grade(english, 93)

    rahul.add_grade(maths, 70)
    rahul.add_grade(science, 65)
    rahul.add_grade(english, 78)

    # 6. PRINT REPORT CARDS
    print("=" * 40)
    print("        REPORT CARDS")
    print("=" * 40)
    for student in classroom.students:
        student.print_report_card()
        print()

    # 7. PRINT CLASSROOM SUMMARY
    classroom.print_summary()

    # 8. TEST ERROR HANDLING
    print("\n--- Testing error handling ---")
    try:
        arjun.add_grade(maths, 150)       # marks exceed max
    except ValueError as e:
        print(f"Caught: {e}")

    try:
        classroom.add_student(Student("Ghost", 1))  # duplicate roll number
    except ValueError as e:
        print(f"Caught: {e}")

    # 9. SAVE AND RELOAD
    classroom.save_to_json("grades.json")
    print("\nSaved to grades.json")

    new_classroom = Classroom("Empty")
    new_classroom.load_from_json("grades.json")
    print(f"Reloaded: {new_classroom}")
    print(f"First student after reload: {new_classroom.students[0]}")

    # 10. CLASS-LEVEL COUNTER
    print(f"\nTotal students ever created: {Student.student_count}")


if __name__ == "__main__":
    main()