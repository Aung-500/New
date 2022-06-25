class Employee:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.pay = 0
        self.bonus = 0

    def register(self):
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
        self.pay = int(input("Enter Pay : "))
        self.bonus = int(input("Enter Bonus : "))

    def totalSalary(self):
        return (self.pay * 12) + self.bonus


if __name__ == "__main__":

    emp1 = Employee()
    emp1.register()
    
    print("Total Salary = %s"%emp1.totalSalary())