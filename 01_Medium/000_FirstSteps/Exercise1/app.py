import datetime
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, welcomme to Keep Calm & Code!"
if __name__ == "__main__":
    app.run(debug=True)


