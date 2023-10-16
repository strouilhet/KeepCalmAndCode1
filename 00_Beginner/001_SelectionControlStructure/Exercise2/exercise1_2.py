def exercise2(photocop):
    if photocop<=10:
        prix=photocop*0.50
    elif photocop <=30:
        prix=10*0.50 + (photocop-10)*0.30
    else:
        prix=10*0.50 + 20*0.30 + (photocop-30)*0.20
    return prix