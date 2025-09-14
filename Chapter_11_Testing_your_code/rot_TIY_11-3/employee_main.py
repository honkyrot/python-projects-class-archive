class Employee:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.salary = 0

    def set_employee(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def give_raise(self, add_to_salary=5000):
        self.salary += add_to_salary

    def get_employee_info(self):
        return f"{self.first_name} {self.last_name} - Salary: {self.salary}"
