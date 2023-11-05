def exercise2(nb):
    if nb==0: binaires=[0]
    else :
        binaires=[]
        i=0
        while nb>0:
            binaires.insert(0,nb%2)
            nb=nb//2
            i=i+1  
    return binaires