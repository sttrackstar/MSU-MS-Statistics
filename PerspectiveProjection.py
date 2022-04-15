import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show
ion()

D=np.array([[3,5,5,3,3,5,5,3],[1,1,0,0,1,1,0,0],[5,5,5,5,4,4,4,4],[1,1,1,1,1,1,1,1]])
C=np.array([
    [0,1,0,1,1,0,0,0],
    [1,0,1,0,0,1,0,0],
    [0,1,0,1,0,0,1,0],
    [1,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,1],
    [0,1,0,0,1,0,1,0],
    [0,0,1,0,0,1,0,1],
    [0,0,0,1,1,0,1,0]])
    
#Perspective Projection at Center(0,0,10)

P1=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,-0.1,1]])
PD1=np.matmul(P1,D)
for j in range(8):
    PD1[:,j]=PD1[:,j]/PD1[3,j]
f, ax1=plt.subplots(1)
for i in range(8):
    for j in range(i):
        if C[i,j]==1:
            ax1.plot([PD1[0,i],PD1[0,j]],[PD1[1,i],PD1[1,j]], 'r-')
ax1.set_title('Center at (0,0,10)')
ax1.axis('off')
show()

#Perspective Projection at Center(10,5,10)

P2=np.array([[1,0,-1,0],[0,1,-0.5,0],[0,0,0,0],[0,0,-0.1,1]])
PD2=np.matmul(P2,D)
#for j in range(8):
# PD2[:,j]=PD2[:,j]/PD2[3,j]
PD2[0,:]=PD2[0,:]/PD2[3,:]
PD2[1,:]=PD2[1,:]/PD2[3,:]
f, ax2=plt.subplots(1)
ax2.plot(PD2[0,:],PD2[1,:],'b.')
for i in range(8):
    for j in range(i):
        if C[i,j]==1:
            ax2.plot([PD2[0,i],PD2[0,j]],[PD2[1,i],PD2[1,j]],'r-')
ax2.set_title('Center at (10,5,10)')
ax2.axis('off')
show()
