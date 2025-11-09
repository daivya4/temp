import numpy as np,random

n=5
dist=[[0,2,3,4,5],[2,0,6,7,8],[3,6,0,9,1],[4,7,9,0,2],[5,8,1,2,0]]

def repair(p):
    r=[]
    for x in p:
        if x not in r: r.append(x)
    for i in range(n):
        if i not in r: r.append(i)
    return r[:n]

def cost(p):
    return sum(dist[p[i]][p[(i+1)%n]] for i in range(n))

pop=[[random.randint(0,n-1) for _ in range(n)] for _ in range(20)]
best=None
bv=999

for it in range(30):
    new=[]
    for _ in range(20):
        p1=random.choice(pop)
        p2=random.choice(pop)
        c=random.randint(1,n-1)
        ch=repair(p1[:c]+p2[c:])
        if random.random()<0.2:
            i,j=random.randint(0,n-1),random.randint(0,n-1)
            ch[i],ch[j]=ch[j],ch[i]
        new.append(ch)
    pop=new
    pop=sorted(pop,key=cost)
    if cost(pop[0])<bv:
        bv=cost(pop[0]);best=pop[0]
    print(it,bv)

print(best,bv)
