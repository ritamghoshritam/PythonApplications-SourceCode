Input :- 

import numpy as num
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

###Defining the metric functions###

def brittle (p,t):
    beta = 0.2;
    mu = (p-beta*(t))/125;
    return mu;

def ductile (p,t):
    temp = 4*(t**2);
    temp = temp + p**2;
    temp = temp/78125;
    mu2 = temp**0.5;    
    return mu2;

###Defining the domain and constructing a mesh###

P = num.linspace(0,125,100);
T = num.linspace(0,125,100);

X,Y = num.meshgrid(P,T);

A = ductile(X,Y);
B = brittle(X,Y);

###Plotting and analyzing the functions###

fig = plt.figure();
ax =plt.axes(projection='3d');

ax.plot_surface(X,Y,A,rstride=1,cstride=1,cmap='coolwarm',edgecolor='none');
ax.plot_surface(X,Y,B,rstride=1,cstride=1,cmap='coolwarm',edgecolor='none');

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(50,60)


###Finding the Intersection of the two membership functions###


PxT = num.transpose([num.tile(P,len(T)),num.repeat(T,len(P))])

Z3=num.array([min(A(i[0],i[1]),B(i[0],i[1]))for i in PxT]).reshape(100,100)
ax.plot_surface(X,Y,Z3,rstride=1,cstride=1,cmap='coolwarm',edgecolor='none');

fig = plt.figure();
ax =plt.axes(projection='3d');
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(50,60)
