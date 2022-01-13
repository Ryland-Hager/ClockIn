from employeeRoutes import employeeRouting
from repositories.Database import database

def setConnection(app):
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite3/dev.db"
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.secret_key = "cop4521"

def initDB(app):
  database.init_app(app)
  database.app = app
  database.create_all()

def setRoutes(app):
  app.register_blueprint(employeeRouting)

def initApp(app):
  setConnection(app)
  initDB(app)
  setRoutes(app)
  