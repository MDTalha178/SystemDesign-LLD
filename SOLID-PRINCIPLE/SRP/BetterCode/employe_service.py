from perfomance_generator_service import PerformanceGeneratorService
from salary_compute_service import SalaryComputeService

class Employee:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
    
    # Perform performance analysis and report results
    def get_address(self):
        print(f"Address of employee {self.name} is {self.address}")

    def employe_data_update(self):
        print(f"Employee {self.name} data is updated")
    

    def get_employee_details(self):
        print(f"Employee {self.name} details are:")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")


e = Employee(101, "Md Talha", "Delhi")

PerformanceGeneratorService().generate_performance_report(e)
SalaryComputeService().salaryCompute(e)