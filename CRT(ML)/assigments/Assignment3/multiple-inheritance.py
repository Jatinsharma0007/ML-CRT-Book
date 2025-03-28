class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def get_payroll_info(self):
        return f"Employee ID: {self.employee_id}, Salary: ${self.salary:.2f}"


class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def manager_summary(self):
        return (
            f"{self.introduce()} "
            f"{self.get_payroll_info()} "
            f"Department: {self.department}, "
            f"Team Size: {self.team_size}"
        )


def main():
    john = Manager(
        name="John Doe",
        age=35,
        employee_id="M001",
        salary=85000,
        department="Engineering",
        team_size=10,
    )

    print("Personal Introduction:")
    print(john.introduce())

    print("\nPayroll Information:")
    print(john.get_payroll_info())

    print("\nManager Summary:")
    print(john.manager_summary())


if __name__ == "__main__":
    main()
