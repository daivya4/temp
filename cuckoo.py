import numpy as np,random

def f(x): return x[0]**2 + np.sin(x[1])*5

n=12
d=2
pa=0.25
pop=[np.random.uniform(-5,5,d) for _ in range(n)]
best=None
bv=1e9

for it in range(30):
    new=[]
    for x in pop:
        step=np.random.normal(0,1,d)*np.random.normal(0,1,d)
        y=x+step
        if f(y)<f(x): x=y
        if random.random()<pa:
            x=np.random.uniform(-5,5,d)
        new.append(x)
    pop=new
    for x in pop:
        v=f(x)
        if v<bv: bv=v;best=x
    print(it,bv)

print(best,bv)
