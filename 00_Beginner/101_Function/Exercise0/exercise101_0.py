t1 = 0.5;
t2 = 0.3;
t3 = 0.2;
q1 = 10;
q2 = 20;

p=0;
n = int(input("nombre de photocopies : "));
if n<q1:
    p=n*t1
else:
    if n<q1+q2:
        p=t1*q1+t2*(n-q1)
    else:
        p=t1*q1+t2*q2+t3*(n-q2-q1)
print("le prix est : "+str(p)+" euros")

