
from flask import Flask
app = Flask(__name__)

@app.route("/index.html")
def index():
    return "page principale"


@app.route("/age.html")
def age():
    age=2
    return "<h2> "+str(age) + "</h2>"


if __name__ == "__main__":
    app.run(debug=True)
