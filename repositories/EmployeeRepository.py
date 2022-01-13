from repositories.EmployeeModel import EmployeeModel
from repositories.Database import database

class EmployeeRepository():
  def insert(self, employee):
    database.session.add(employee)
    database.session.commit()
  
  def getAll(self):
    all = EmployeeModel.query.all()
    return all

  def update(self, updatedEmployeeDTO):
    oldEmployee = EmployeeModel.query.filter_by(id = updatedEmployeeDTO.id).first()
    oldEmployee.name = updatedEmployeeDTO.name
    oldEmployee.phoneNumber = updatedEmployeeDTO.phoneNumber
    database.session.commit()

  def deleteById(self, id):
    e = EmployeeModel.query.get(id)
    database.session.delete(e)
    database.session.commit()
