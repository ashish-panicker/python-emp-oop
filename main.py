from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")  
    @abstractmethod
    def calculate_salary(self):
        pass
class PermanentEmployee(Employee):
    def __init__(self, name, employee_id, department, base_salary, bonus):
        super().__init__(name, employee_id, department)
        self.base_salary = base_salary
        self.bonus = bonus
    def calculate_salary(self):
        return self.base_salary + self.bonus
    def display_details(self):
        super().display_details()
        print(f"Base Salary: {self.base_salary}")
        print(f"Bonus: {self.bonus}")
        print(f"Total Salary: {self.calculate_salary()}")
class ContractEmployee(Employee):
    def __init__(self, name, employee_id, department, hourly_rate, hours_worked):
        super().__init__(name, employee_id, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: {self.hourly_rate}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Total Salary: {self.calculate_salary()}")
class Intern(Employee):
    def __init__(self, name, employee_id, department, stipend):
        super().__init__(name, employee_id, department)
        self.stipend = stipend
    def calculate_salary(self):
        return self.stipend
    def display_details(self):
        super().display_details()
        print(f"Stipend: {self.stipend}")
        print(f"Total Salary: {self.calculate_salary()}")
def main():
    emp1 = PermanentEmployee("Migule", "101", "HR", 100000, 10000)
    emp2 = ContractEmployee("Miles", "102", "IT", 50, 150)
    emp3 = Intern("Gwen", "103", "Marketing", 2000)
    employees = [emp1, emp2, emp3]
    for emp in employees:
        print("\nEmployee Details:")
        emp.display_details()
        print("-" * 30)
if __name__ == "__main__":
    main()
