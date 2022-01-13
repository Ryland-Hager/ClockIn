
from repositories.Database import database

class EmployeeModel(database.Model):
  __table_args__ = {'extend_existing': True}
  id = database.Column(database.Integer, primary_key = True)
  name = database.Column(database.String(225))
  phoneNumber = database.Column(database.String(20))

  def __init__(self, name, phoneNumber):
    self.name = name
    self.phoneNumber = phoneNumber