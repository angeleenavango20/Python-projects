class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def display(self):
        print("Role: ", self.role)
        print("Department: ", self.dept)
        print("Salary: ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 70000)

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        super().display()

eng1 = Engineer("Alice", 30)
eng1.display()
      