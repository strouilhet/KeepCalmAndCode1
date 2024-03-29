from datetime import datetime
from flask import Flask

def age(an, mois, jour):
    date=datetime.now()
    anC=date.year
    moisC=date.month
    jourC=date.day
    if mois < moisC: # l'anniversaire est passé
        age=str(anC-an)+" ans "
        if jour < jourC:
            age=age+ str(moisC-mois)+" mois "
            age=age+str(jourC-jour)+" jours"
        else: 
            age=age+ str(12-mois+moisC)+" mois "
            age=age+str(31-jour+jourC)+" jours"
    else :
        if jour <= jourC: # anniversaire passé
            age=str(anC-an)+" ans "
            age=age+ str(moisC-mois)+" mois "
            age=age+str(jourC-jour)+" jours"
        else: 
            age=str(anC-an-1)+" ans "
            age=age+ str(12-mois+moisC-1)+" mois "
            age=age+str(31-jour+jourC)+" jours"
    return age

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, j'ai "+ str(age(2000, 10, 21))
if __name__ == "__main__":
    app.run(debug=True)


