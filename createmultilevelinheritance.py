class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(people):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager_info(self):
        print("\n--- Manager Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary}")
        print(f"Department: {self.department}")

    def approve_leave(self):
        print(f"{self.name} has approved the leave request.")


managerdetail1 = Manager(
    name="Sudhir Patel",
    age=35,
    employee_id="231256",
    salary=95000,
    department="CSE"
)

managerdetail1.display_manager_info()
managerdetail1.approve_leave()