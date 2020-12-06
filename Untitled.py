#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math
import scipy.stats
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
r=0.59
d=[]    
angle=11/18       ## Angle change here
for i in range(100):
    R3rna=np.array([0,0,0])
    theta=np.random.uniform(0,2*math.pi)
    phi=np.random.uniform(0,math.pi)
    rna=np.array([0,phi,theta])
    [x,y,z]=[r*math.sin(theta)*math.cos(phi),r*math.sin(theta)*math.sin(phi),r*math.cos(theta)]
    R3rna=R3rna+np.array([x,y,z])
    x1=[]
    y1=[]
    z1=[]
    x1.append(R3rna[0])
    y1.append(R3rna[1])
    z1.append(R3rna[2])
    for i in range(6636-30*0):    ## Apply changes in nts number, Apply ribosome number change here as well!     
        [a,b,c]=rna
        c=math.pi/2-c
        phi=np.random.uniform(b-math.pi*angle,b+math.pi*angle)
        theta1=np.random.uniform(c-math.pi*angle,c+math.pi*angle)
        theta=math.pi/2-theta1
        rna=np.array([0,phi,theta])
        [x,y,z]=[r*math.sin(theta)*math.cos(phi),r*math.sin(theta)*math.sin(phi),r*math.cos(theta)]
        R3rna=R3rna+np.array([x,y,z])
        x1.append(R3rna[0])
        y1.append(R3rna[1])
        z1.append(R3rna[2])
    def ribosome(number):
        length=np.size(x1)
        var=0
        while var < number:
            num=np.random.randint(0,length-1)
            a1=x1[num+1]-x1[num]
            b1=y1[num+1]-y1[num]
            c1=z1[num+1]-z1[num]
            if math.sqrt(a1**2+b1**2+c1**2)<1:
               a1=30*a1        
               b1=30*b1
               c1=30*c1
               for i in range(length-num):
                   x1[num+i]=x1[num+i]+a1
                   y1[num+i]=y1[num+i]+b1
                   z1[num+i]=z1[num+i]+c1
               var=var+1
            else:
                var=var
    ribosome(0)    ## Change ribosome number 
    distance=math.sqrt(x1[-1]**2+y1[-1]**2+z1[-1]**2)
    d.append(distance)
d=np.array(d)
xmin=np.min(d)
xmax=np.max(d)
mean,std=scipy.stats.norm.fit(d)
median=np.median(d)
plt.hist(d, bins=25, density=True, alpha=0.6, color='g')
x = np.linspace(xmin, xmax, 100)
y = scipy.stats.norm.pdf(x, mean, std)
plt.plot(x, y, 'k', linewidth=2)
title = "Fit results: mean = %.2f, median=%.2f, std = %.2f" % (mean,median, std)
plt.title(title)
plt.show()

