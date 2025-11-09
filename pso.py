import numpy as np,random

def f(x): return x[0]**2 + 4*x[1]**2

n=25
d=2
pos=[np.random.uniform(-5,5,d) for _ in range(n)]
vel=[np.zeros(d) for _ in range(n)]
pbest=pos.copy()
pbv=[f(x) for x in pos]
gbest=pbest[np.argmin(pbv)]

for it in range(30):
    for i in range(n):
        r1=np.random.rand()
        r2=np.random.rand()
        vel[i]=0.7*vel[i]+1.5*r1*(pbest[i]-pos[i])+1.5*r2*(gbest-pos[i])
        pos[i]=pos[i]+vel[i]
        v=f(pos[i])
        if v<pbv[i]:
            pbv[i]=v
            pbest[i]=pos[i]
    gbest=pbest[np.argmin(pbv)]
    print(it,f(gbest))

print(gbest,f(gbest))
