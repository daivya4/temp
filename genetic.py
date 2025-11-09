import random

jobs=[3,5,2,7,4,6]
m=3

def fit(ch):
    load=[0]*m
    for i,mc in enumerate(ch): load[mc]+=jobs[i]
    return max(load)

pop=[[random.randint(0,m-1) for _ in jobs] for _ in range(30)]
best=None
bv=999

for it in range(30):
    pop=sorted(pop,key=fit)
    new=pop[:5]
    while len(new)<30:
        p1=random.choice(pop[:10])
        p2=random.choice(pop[:10])
        c=random.randint(1,len(jobs)-2)
        ch=p1[:c]+p2[c:]
        if random.random()<0.2:
            i=random.randint(0,len(jobs)-1)
            ch[i]=random.randint(0,m-1)
        new.append(ch)
    pop=new
    if fit(pop[0])<bv: bv=fit(pop[0]);best=pop[0]
    print(it,bv)

print(best,bv)
