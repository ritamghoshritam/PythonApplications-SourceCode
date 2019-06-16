import numpy as np
import matplotlib.pyplot as plt gf = plt.figure()
ga = gf.add_subplot(111, projection='3d')
def maxMin(x, y): z = []
for x1 in x: for y1 in y.T:
z.append(max(np.minimum(x1, y1))) return np.array(z).reshape((x.shape[0], y.shape[1]))
def composition():
P=np.array([0.2,0.6,0.5,0.9])
Q=np.array([0.4,0.7,0.8]) C=np.zeros(shape=(4,3))
for i in range(4):
for j in range(3): if(P[i]<Q[j]):
C[i][j]=P[i] else: C[i][j]=Q[j]
D=np.array([[0.3,0.6,0.5,0.2,0.1],
[0.4,0.7,0.5,0.3,0.3],
[0.2,0.6,0.8,0.9,0.8]])
T=np.zeros(shape=(4,5))
U=maxMin(C,D) print("The cartesian product of P and Q is:") print(R)
print("The composition of matrix C and D is :")
print(U) x=range(5) y=range(4)
X, Y = np.meshgrid(x, y) ga.plot_surface(X, Y, U) plt.show() composition()
