from datetime import date

def exercise0(jour, mois, an):
    #dateC=date.today()
    anC=2030 #dateC.year
    moisC=1 #dateC.month
    jourC=1 #dateC.day
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


print(exercise0(13,10,2020))