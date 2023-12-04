
from datetime import datetime
from datetime import date

from flask import Flask

def calculerAge(an, mois, jour):
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

@app.route("/age.html")
def age():
   return "Hello, j'ai <h2>"+ str(calculerAge(2000, 10, 21))+ "</h2> ans"

@app.route("/heure.html")
def heure():
    heure= datetime.now().hour
    jour = datetime.now().weekday()
    rep="<h1> Repos </h1>"
    if jour >=0 and jour <=4 and heure >=8 and heure <18:
        rep="Travail"
    return rep

@app.route("/jour.html")
def jour():
    delta=date(datetime.today().year, 12, 31)- date(datetime.today().year,datetime.today().month,datetime.today().day)
    return "Il reste "+str(delta.days)+" jours avant la fin de l'année"


if __name__ == "__main__":
    app.run(debug=True)
