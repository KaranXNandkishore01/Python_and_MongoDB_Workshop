class Employee:
    def __init__(self, name, emp_id, emplylocation,mob):
        self.name = name
        self.emp_id = emp_id
        self.emplylocation = emplylocation
        self.mob = mob
        
    def show(self): 
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Location:", self.emplylocation)
        print("Mobile No:", self.mob)
        print("*****************")

# Creating objects
d1 = Employee("Karan", 101, "Delhi", 9876543210)
d1.show()

d2 = Employee("Rahul", 102, "Indore", 8765432109)
d2.show()

d3 = Employee("Ankit", 103, "Bhopal", 7654321098)
d3.show()
