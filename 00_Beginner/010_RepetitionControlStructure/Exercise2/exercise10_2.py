def exercise2(nb):
    # trouver la puissance
    reste=nb
    puissance=0
    while reste !=0:
        puissance=puissance+1
        reste=reste//10
    reste=nb    
    calcul=0
    while reste !=0:
        chiffre=reste%10
        reste=reste//10
        # ou reste=(reste - chiffre)/10
        calcul=calcul+chiffre**puissance
    return nb==calcul