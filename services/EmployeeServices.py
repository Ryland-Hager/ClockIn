from repositories.EmployeeModel import EmployeeModel
from repositories.EmployeeRepository import EmployeeRepository

class EmployeeServices():
  def __init__(self):
    self.employeeRepo = EmployeeRepository()
    
  def addNewEmployee(self, employeeDTO):
    employee = EmployeeModel(employeeDTO.name, employeeDTO.phoneNumber)
    self.employeeRepo.insert(employee)
  
  def getAll(self):
    return self.employeeRepo.getAll()
  
  def update(self, employeeDTO):
    self.employeeRepo.update(employeeDTO)
    
  def deleteById(self, id):
    self.employeeRepo.deleteById(id)
