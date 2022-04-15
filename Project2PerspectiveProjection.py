import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show
ion()

D=np.array([[-6.5,-6.5,-6.5,-6.5,-2.5,-2.5,-0.75,-0.75,3.25,3.25,4.5,4.5,6.5,6.5,6.5,6.5],
            [-2,-2,0.5,0.5,0.5,0.5,2,2,2,2,0.5,0.5,0.5,0.5,-2,-2],
            [-2.5,2.5,2.5,-2.5,-2.5,2.5,-2.5,2.5,-2.5,2.5,-2.5,2.5,-2.5,2.5,2.5,-2.5],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])

C=np.array([[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]])
            
#Question #1
#Perspective Projection at Center(-5,10,10)
P1=np.array([[1,0,0.5,0],[0,1,-1,0],[0,0,0,0],[0,0,-0.1,1]])
PD1=np.matmul(P1,D)
for j in range(16):
    PD1[:,j]=PD1[:,j]/PD1[3,j]
f, ax1=plt.subplots(1)
for i in range(16):
    for j in range(i):
        if C[i,j]==1:
            ax1.plot([PD1[0,i],PD1[0,j]],[PD1[1,i],PD1[1,j]], 'purple')
ax1.set_title('Center at (-5,10,10)')
ax1.axis('off')
show()

#Question #2
#Perspective Projection at Center(0,10,25)

P2=np.array([[1,0,0,0],[0,1,-0.4,0],[0,0,0,0],[0,0,-0.04,1]])
PD2=np.matmul(P2,D)
for j in range(16):
    PD2[:,j]=PD2[:,j]/PD2[3,j]
f, ax2=plt.subplots(1)
for i in range(16):
    for j in range(i):
        if C[i,j]==1:
            ax2.plot([PD2[0,i],PD2[0,j]],[PD2[1,i],PD2[1,j]], 'purple')
ax2.set_title('Center at (0,10,25)')
ax2.axis('on')
show()

#Question #3
#Rotation of Toyota 30 degrees about the y-axis with Perspective Projection at Center(0,10,25)
phi=30
R=np.array([[math.cos(phi),0,math.sin(phi),0],[0,1,0,0],[-math.sin(phi),0,math.cos(phi),0],[0,0,0,1]])
DR=np.matmul(R, D)
P3=np.array([[1,0,0,0],[0,1,-0.4,0],[0,0,0,0],[0,0,-0.04,1]])
PD3=np.matmul(P3,D)
RPD3=np.matmul(R, PD3)
for j in range(16):
    PD3[:,j]=PD3[:,j]/PD3[3,j]
f, ax3=plt.subplots(1)
for i in range(16):
    for j in range(i):
        if C[i,j]==1:
            ax3.plot([RPD3[0,i],RPD3[0,j]],[RPD3[1,i],RPD3[1,j]], 'purple')
ax3.set_title('Center at (0,10,25)')
ax3.axis('off')
show()

#Question #4
#Rotation of Toyota 45 degrees about the z-axis with Perspective Projection at Center(0,10,25)
phi=45
R=np.array([[math.cos(phi),-math.sin(phi),0,0],[math.sin(phi),math.cos(phi),0,0],[0,0,1,0],[0,0,0,1]])
DR=np.matmul(R, D)
P4=np.array([[1,0,0,0],[0,1,-0.4,0],[0,0,0,0],[0,0,-0.04,1]])
PD4=np.matmul(P4,D)
RPD4=np.matmul(R, PD4)
for j in range(16):
    PD4[:,j]=PD4[:,j]/PD4[3,j]
f, ax4=plt.subplots(1)
for i in range(16):
    for j in range(i):
        if C[i,j]==1:
            ax4.plot([RPD4[0,i],RPD4[0,j]],[RPD4[1,i],RPD4[1,j]], 'purple')
ax4.set_title('Center at (0,10,25)')
ax4.axis('off')
show()

#Question #5
#Zoom in Toyota 150%
S=np.array([[1.5,0,0,0],[0,1.5,0,0],[0,0,1.5,0],[0,0,0,1]])
DS=np.matmul(S, D)
P5=np.array([[1,0,0,0],[0,1,-0.4,0],[0,0,0,0],[0,0,-0.04,1]])
PD5=np.matmul(P5,D)
SPD5=np.matmul(S, PD5)
f, ax5=plt.subplots(1)
for i in range(16):
    for j in range(i):
        if C[i,j]==1:
            ax5.plot([SPD5[0,i],SPD5[0,j]],[SPD5[1,i],SPD5[1,j]], 'purple')
ax5.set_title('Center at (0,10,25)')
ax5.axis('on')
show()
