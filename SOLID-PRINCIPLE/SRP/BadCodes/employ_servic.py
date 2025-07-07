class Employee:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
    
    # Perform performance analysis and report results
    def print_performance_report(self):
        print(f"Employee {self.name} performance report:")
    
    def salaryCompute(self):
        print(f"Employee {self.name} salary is: 100000")
    

    def employe_data_update(self):
        print(f"Employee {self.name} data is updated")
    

    def get_employee_details(self):
        print(f"Employee {self.name} details are:")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
