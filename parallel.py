import numpy as np

grid=np.random.randint(0,2,(20,20))
for it in range(20):
    new=grid.copy()
    for i in range(20):
        for j in range(20):
            ne=grid[max(0,i-1):i+2,max(0,j-1):j+2]
            s=ne.sum()
            new[i][j]=1 if s%3==0 else 0
    grid=new
    print(it,grid.sum())
