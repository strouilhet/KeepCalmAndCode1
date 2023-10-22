def exercise1():
    i=1000
    trouve=False
    while i<10000 and not trouve:
        mille=i//1000
        cent=i//100%10
        dix=i//10%10
        un=i%10
        if mille%2==0 and mille+cent==15 and cent-mille==dix and un*dix==mille:
            trouve=True
        else: i=i+1
    return i

