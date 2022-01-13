from mapper.object_mapper import ObjectMapper
from models.Employee import Employee
from services.DTOs.EmployeeDTO import EmployeeDTO

class EmployeeMapper:
  def __init__(self):
    self.Employee_to_DTO = ObjectMapper()
    self.DTO_to_Employee = ObjectMapper()
    
    def employee_to_DTO(self):
      self.Employee_to_DTO.create_map(type_from = type(Employee), type_to = type(EmployeeDTO))
      return self.Employee_to_DTO
    
    def dto_to_Employee(self):
      self.DTO_to_Employee.create_map(type_from = type(EmployeeDTO), type_to = type(Employee))
      return self.DTO_to_Employee