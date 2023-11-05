def exercise1(nb):
    tab=[]
    i=0
    while nb>0:
        j=int(nb%10)
        tab.append(j)
        i=i+1
        nb=nb//10
        print(nb)
    return tab

print(exercise1(234))

