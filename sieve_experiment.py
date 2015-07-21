# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 17:36:38 2014

@author: rossi

A sieve simulation program.
"""

from scipy import *
from scipy.special import lambertw
from numpy.random import uniform,permutation

import matplotlib.backends.backend_agg as agg
import pygame
import matplotlib.pyplot as plt
 
class sieve_experiment():

    def __init__(self,m,n,iterations):
        self.n = n
        self.iterations=iterations
        phi0 = 1.*m/n
        smallPores = [m]
        for i in range(1,iterations):
            if (uniform(0,smallPores[-1] + n) < n):
                smallPores.append(smallPores[-1])
            else:
                smallPores.append(smallPores[-1]-1)
        self.smallPores = array(smallPores)
        
        T = 1.0*iterations/n
        simphi = double(smallPores)/n
        self.simp = simphi/(1.+simphi)
        self.sims = r_[0:T:iterations*1.j]
        self.s = r_[0:T:1000j]

        c = log(phi0*exp(phi0))
        self.phi = lambertw(exp(-self.s+c)).real
        self.p = self.phi/(1.+self.phi)

def CreatePlot(experiment,ind):
    fig = plt.figure(figsize=[6, 4], dpi=100)
    ax = fig.gca()
    ax.plot(experiment.s,experiment.p,'c')
    ax.plot(experiment.sims[:ind],experiment.simp[:ind],'xb')
    plt.xlabel('time (t)',fontsize=12)
    plt.title('Probability',fontsize=12)
    ax.legend(('Theory','Experiment'),numpoints=1)
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_argb()
    return(fig,raw_data,canvas)

def ParticleFall(ind,surf):
    size2 = canvas.get_width_height()

    for j in range(0,size[1],2):
        disp.blit(surf, ((size[0]-size2[0])/2,0))
        x = int((pos[ind]+size[0]/2.)/2. + (size[0]/2.-pos[ind])*(cos(pi*j/size[1]))/2.)
        pygame.draw.rect(disp,(200,0,200),(x,j,3,3))
        pygame.display.flip()
        pygame.draw.rect(disp,(0,0,0),(x,j,3,3))
        
def ParticleStuck(ind,surf):
    for j in range(0,size[1]-21,2):
        disp.blit(surf, ((size[0]-size2[0])/2,0))
        x = int((pos[ind]+size[0]/2.)/2. + (size[0]/2.-pos[ind])*(cos(pi*j/(size[1]-21)))/2.)
        pygame.draw.rect(disp,(200,0,200),(x,j,3,3))
        pygame.display.flip()
        pygame.draw.rect(disp,(0,0,0),(x,j,3,3))
    pygame.draw.rect(disp,(255,0,0),(pos[ind],size[1]-23,2,2))
    pygame.display.flip()

# Draw the sieve.  Scramble the locations of the small pores.
def DrawSieve(disp):
    pos = map(int,size[0]/(m+n+1.)*r_[0:m+n]+2.5)
    arrangement = permutation(n+m)

    pygame.draw.rect(disp,(0,255,0),(0,size[1]-20,size[0],20))
    for k in arange(len(pos)):
        if (arrangement[k] >= m):
            pygame.draw.rect(disp,(0,0,0),(pos[k]-1,size[1]-20,3,20))
        else:
            pygame.draw.rect(disp,(0,0,0),(pos[k],size[1]-20,1,20))
    pygame.display.flip()
    return(pos,arrangement)
    
size = (600,500)
pygame.init()
disp = pygame.display.set_mode(size)
disp.fill((0,0,0))

m = 100
n = 20
duration = 300

experiment = sieve_experiment(m,n,duration)
pos,arrangement = DrawSieve(disp)

for its in range(1,duration):
    fig,raw_data,canvas = CreatePlot(experiment,its)
    if (its == 1):
        size2 = canvas.get_width_height()
        
    surf = pygame.image.fromstring(raw_data, size2, "ARGB")
    if (experiment.smallPores[its-1] == experiment.smallPores[its]):
        # Fall into the next large pore.
        q = int(uniform(0,m+n))
        while (arrangement[q] < m):
            q = int(uniform(0,m+n))
        ParticleFall(q,surf)
    else:
        # Fall into the next small pore.
        idx = argwhere(arrangement == experiment.smallPores[its])
        idx = idx[0][0]
        ParticleStuck(idx,surf)
    plt.close(fig)