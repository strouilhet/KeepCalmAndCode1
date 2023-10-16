def exercise4(an):
    rep= False
    if (an%4==0 and an%100 !=0 or an%400==0):
        rep=True
    return rep