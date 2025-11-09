import numpy as np, random

dist=np.array([[0,2,9,10],[1,0,6,4],[15,7,0,8],[6,3,12,0]])
n=len(dist)
ants=5;alpha=1;beta=5;rho=0.5;Q=100

pher=np.ones((n,n))/n
best=float('inf');bp=[]

def length(p):
    return sum(dist[p[i]][p[(i+1)%n]] for i in range(n))

for it in range(20):
    paths=[];lens=[]
    for a in range(ants):
        c=random.randint(0,n-1)
        vis={c}
        path=[c]
        while len(path)<n:
            pr=[]
            for j in range(n):
                if j in vis: pr.append(0)
                else:
                    pr.append((pher[c][j]**alpha)*((1/dist[c][j])**beta))
            pr=np.array(pr);pr/=pr.sum()
            nx=np.random.choice(range(n),p=pr)
            path.append(nx);vis.add(nx);c=nx
        L=length(path)
        paths.append(path);lens.append(L)
        if L<best: best=L;bp=path
    pher=(1-rho)*pher
    for p,L in zip(paths,lens):
        for i in range(n):
            a,b=p[i],p[(i+1)%n]
            pher[a][b]+=Q/L;pher[b][a]+=Q/L
    print(it,best)

print("BEST",bp,best)
