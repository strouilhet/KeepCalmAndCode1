def exercise1(nb):
    if nb<6:
        rep="pas assez"
    else : 
        boites=0
        while nb>=6:
            boites=boites+1
            nb=nb-6
        rep=str(boites)+ " boîtes et "+str(nb)+" oeufs"
    return rep
    

