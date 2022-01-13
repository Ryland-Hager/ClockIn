from flask import render_template, Flask
from App import initApp

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

if __name__ == "__main__":
  initApp(app)
  app.run(debug=True)