def exercise1(a,b,c):
    if (a==b):
        if (b==c):
            rep="three equal"
        else: rep="two equal"
    elif (b==c):   
        rep="two equal" 
    elif (a==c):
        rep="two equal"
    else: 
        rep="all different"
    return rep
