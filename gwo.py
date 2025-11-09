import numpy as np,random

def f(x): return 3*x[0]**2 + x[1]**2

wolves=20
d=2
pop=[np.random.uniform(-5,5,d) for _ in range(wolves)]
best=None
bv=1e9

for it in range(30):
    pop=sorted(pop,key=f)
    a=2*(1-it/30)
    al,be,de=pop[0],pop[1],pop[2]
    new=[]
    for x in pop:
        r1=np.random.rand(d);r2=np.random.rand(d)
        A1=2*a*r1-a
        C1=2*r2
        X1=al-A1*abs(C1*al-x)

        r1=np.random.rand(d);r2=np.random.rand(d)
        A2=2*a*r1-a
        C2=2*r2
        X2=be-A2*abs(C2*be-x)

        r1=np.random.rand(d);r2=np.random.rand(d)
        A3=2*a*r1-a
        C3=2*r2
        X3=de-A3*abs(C3*de-x)

        new.append((X1+X2+X3)/3)
    pop=new
    if f(pop[0])<bv: bv=f(pop[0]);best=pop[0]
    print(it,bv)

print(best,bv)
