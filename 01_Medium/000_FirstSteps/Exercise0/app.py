
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, welcome to Keep Calm & Code!"
if __name__ == "__main__":
    app.run(debug=True)
