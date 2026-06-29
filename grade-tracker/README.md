# Student Grade Tracker

A command-line app to manage students and grades, built with Python OOP.

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
