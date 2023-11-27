
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/index.html")
def index():
   return render_template('index.html')

@app.route("/reponse.html")
def reponse():
   rep=2023 - int(request.args.get('annee'))
   return render_template('reponse.html', age=rep)

if __name__ == "__main__":
    app.run(debug=True)
