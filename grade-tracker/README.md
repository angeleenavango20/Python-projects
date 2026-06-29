# Student Grade Tracker

A command-line Python project for managing students, subjects, and grades — built with object-oriented programming.

## What it does

- Add students to a classroom and assign grades per subject
- Calculate each student's average and percentage automatically
- Print formatted report cards and classroom rankings
- Save and reload all data from a JSON file
- Handles invalid input with proper error messages

## Structure
```
grade_tracker/
├── tracker/
│   ├── __init__.py
│   ├── person.py      ← base class
│   ├── subject.py     ← subject with max marks
│   ├── student.py     ← inherits Person, stores grades
│   └── classroom.py   ← manages a list of students
└── main.py            ← entry point
```

## Run
```bash
python main.py
```

## Concepts practised
- Classes and __init__
- Inheritance and super()
- Dunder methods: __str__, __repr__, __eq__, __lt__, __len__
- Class-level attributes (student_count)
- Packages and imports
- JSON file I/O
- Input validation with ValueError
