from flask import render_template, Blueprint, abort, request, redirect, url_for
from jinja2 import TemplateNotFound

from repositories.EmployeeModel import EmployeeModel
from services.DTOs.EmployeeDTO import EmployeeDTO
from services.EmployeeServices import EmployeeServices

employeeServices = EmployeeServices()

employeeRouting = Blueprint('Employee', __name__,
                        template_folder='templates')

@employeeRouting.route("/Employee", methods=["GET"])
def employeeIndex():
  try:
    allEmp = employeeServices.getAll()
    return render_template("Employee/employeeIndex.html", employees = allEmp)
  except TemplateNotFound:
    abort(404)
    
@employeeRouting.route("/Employee", methods=["POST"])
def addEmployee():
  emp = EmployeeDTO(None, request.form["name"], request.form["phoneNumber"])
  employeeServices.addNewEmployee(emp)
  
  return redirect(url_for("Employee.employeeIndex"))

@employeeRouting.route("/update", methods=["POST"])
def updateEmployee():
  dto = EmployeeDTO(request.form["id"], request.form["name"], request.form["phoneNumber"])
  employeeServices.update(dto)
  
  return redirect(url_for("Employee.employeeIndex"))

  
@employeeRouting.route("/delete/<string:id>", methods=["POST", "GET"])
def delete(id):
  employeeServices.deleteById(id)

  return redirect(url_for("Employee.employeeIndex"))
